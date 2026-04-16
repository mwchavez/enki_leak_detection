from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix

from pathlib import Path as _Path
import sys as _sys

ROOT = _Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in _sys.path:
    _sys.path.insert(0, str(SRC))

from scaler_utils import apply_standard_scaler, load_scaler_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the binary leak classifier on a held-out feature set.")
    parser.add_argument(
        "--model",
        type=Path,
        default=ROOT / "models" / "leak_binary_classifier.keras",
        help="Path to saved Keras model.",
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=ROOT / "models" / "test_set.csv",
        help="Feature CSV to evaluate.",
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
        help="JSON file with scaler parameters.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
        help="Decision threshold for leak prediction.",
    )
    args = parser.parse_args()

    model = tf.keras.models.load_model(args.model)
    df = pd.read_csv(args.dataset)

    with args.feature_columns.open("r", encoding="utf-8") as handle:
        feature_columns = json.load(handle)["feature_columns"]
    _, means, stds = load_scaler_json(args.scaler)

    x = df[feature_columns].fillna(0.0).to_numpy(dtype="float32")
    x_scaled = apply_standard_scaler(x, means, stds)
    y_true = (df["label"] == "leak").astype("int32").to_numpy()

    probabilities = model.predict(x_scaled, verbose=0).reshape(-1)
    y_pred = (probabilities >= args.threshold).astype("int32")

    labels = ["no_leak", "leak"]
    matrix = confusion_matrix(y_true, y_pred, labels=[0, 1])
    report = classification_report(y_true, y_pred, target_names=labels, digits=4, zero_division=0)

    matrix_df = pd.DataFrame(matrix, index=labels, columns=labels)
    matrix_path = args.dataset.parent / "confusion_matrix.csv"
    report_path = args.dataset.parent / "classification_report.txt"
    prediction_path = args.dataset.parent / "predictions.csv"
    matrix_df.to_csv(matrix_path)
    report_path.write_text(report, encoding="utf-8")

    output_df = df.copy()
    output_df["leak_probability"] = probabilities
    output_df["predicted_label"] = ["leak" if value else "no_leak" for value in y_pred]
    output_df.to_csv(prediction_path, index=False)

    print(report)
    print(f"Saved confusion matrix to {matrix_path}")


if __name__ == "__main__":
    main()
