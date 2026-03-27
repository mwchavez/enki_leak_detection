from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf

from pathlib import Path as _Path
import sys as _sys

ROOT = _Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in _sys.path:
    _sys.path.insert(0, str(SRC))

from scaler_utils import apply_standard_scaler, load_scaler_json


def to_python_int_list(values) -> list[int]:
    return [int(value) for value in values]


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert the trained binary leak model to TensorFlow Lite.")
    parser.add_argument(
        "--model",
        type=Path,
        default=ROOT / "models" / "leak_binary_classifier.keras",
        help="Path to saved Keras model.",
    )
    parser.add_argument(
        "--representative-data",
        type=Path,
        default=ROOT / "models" / "train_set.csv",
        help="Feature CSV used to build a representative dataset for quantization.",
    )
    parser.add_argument(
        "--feature-columns",
        type=Path,
        default=ROOT / "models" / "feature_columns.json",
        help="JSON file with ordered feature columns.",
    )
    parser.add_argument(
        "--scaler",
        type=Path,
        default=ROOT / "models" / "scaler_params.json",
        help="JSON file with feature scaling parameters.",
    )
    parser.add_argument(
        "--quantize",
        choices=["none", "int8"],
        default="none",
        help="Whether to export a float32 or full int8 model.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional custom output path.",
    )
    parser.add_argument(
        "--metadata-output",
        type=Path,
        default=None,
        help="Optional metadata JSON output path.",
    )
    parser.add_argument(
        "--representative-limit",
        type=int,
        default=100,
        help="Maximum number of representative samples for quantization.",
    )
    args = parser.parse_args()

    model = tf.keras.models.load_model(args.model)
    df = pd.read_csv(args.representative_data)

    with args.feature_columns.open("r", encoding="utf-8") as handle:
        feature_columns = json.load(handle)["feature_columns"]
    _, means, stds = load_scaler_json(args.scaler)

    features = df[feature_columns].fillna(0.0).to_numpy(dtype=np.float32)
    scaled_features = apply_standard_scaler(features, means, stds)

    if args.output is None:
        file_name = "leak_model_int8.tflite" if args.quantize == "int8" else "leak_model_float.tflite"
        output_path = ROOT / "exports" / file_name
    else:
        output_path = args.output

    if args.metadata_output is None:
        metadata_path = output_path.with_name(output_path.stem + "_metadata.json")
    else:
        metadata_path = args.metadata_output

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    if args.quantize == "int8":
        representative = scaled_features[: min(len(scaled_features), args.representative_limit)]

        def representative_dataset():
            for row in representative:
                yield [np.expand_dims(row.astype(np.float32), axis=0)]

        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.representative_dataset = representative_dataset
        converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        converter.inference_input_type = tf.int8
        converter.inference_output_type = tf.int8

    tflite_model = converter.convert()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(tflite_model)

    interpreter = tf.lite.Interpreter(model_content=tflite_model)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()[0]
    output_details = interpreter.get_output_details()[0]

    metadata = {
        "model_path": str(output_path),
        "quantize": args.quantize,
        "model_size_bytes": len(tflite_model),
        "input_shape": to_python_int_list(input_details["shape"]),
        "input_dtype": str(input_details["dtype"]),
        "input_scale": float(input_details["quantization"][0]),
        "input_zero_point": int(input_details["quantization"][1]),
        "output_shape": to_python_int_list(output_details["shape"]),
        "output_dtype": str(output_details["dtype"]),
        "output_scale": float(output_details["quantization"][0]),
        "output_zero_point": int(output_details["quantization"][1]),
        "requires_external_scaling": True,
        "scaler_header": "scaler_params.h",
    }
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
