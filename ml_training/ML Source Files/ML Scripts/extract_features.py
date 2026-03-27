from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_utils import ensure_parent, load_config, read_wav_mono
from features import build_feature_record, feature_column_names


def resolve_audio_path(audio_path_value: str, manifest_path: Path) -> Path:
    audio_path = Path(audio_path_value)
    if audio_path.is_absolute():
        return audio_path
    return (manifest_path.parent / audio_path).resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract Arduino-aligned feature vectors from WAV files.")
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "configs" / "experiment.json",
        help="Path to experiment configuration.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "data" / "manifest.csv",
        help="Input manifest CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "data" / "features" / "features.csv",
        help="Output feature CSV path.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    df = pd.read_csv(args.manifest)
    feature_names = feature_column_names(config)

    records: list[dict] = []
    for index, row in df.iterrows():
        audio_path = resolve_audio_path(str(row["audio_path"]), args.manifest)
        audio = read_wav_mono(audio_path, int(config["sample_rate"]))
        metadata = row.to_dict()

        feature_record = build_feature_record(audio, config, metadata)
        ordered_record = {name: feature_record[name] for name in feature_names}

        output_row = row.to_dict()
        output_row["audio_path"] = str(audio_path)
        output_row.update(ordered_record)
        records.append(output_row)

        if (index + 1) % 25 == 0:
            print(f"Processed {index + 1} clips")

    output_df = pd.DataFrame(records)
    ensure_parent(args.output)
    output_df.to_csv(args.output, index=False)
    print(f"Saved {len(output_df)} feature rows to {args.output}")


if __name__ == "__main__":
    main()
