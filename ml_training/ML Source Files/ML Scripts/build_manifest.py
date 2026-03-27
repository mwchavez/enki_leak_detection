from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_utils import load_config, write_csv


def infer_session_id(audio_path: Path) -> str:
    return audio_path.stem.split("__")[0]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a manifest from label folders under ml/data/raw.")
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "configs" / "experiment.json",
        help="Path to experiment configuration.",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=ROOT / "data" / "raw",
        help="Directory containing one folder per raw label.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "data" / "manifest.csv",
        help="Manifest CSV output path.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    output_parent = args.output.parent.resolve()
    label_map = dict(config["label_map"])
    leak_size_map = dict(config["leak_size_map"])

    rows: list[dict] = []
    fieldnames = [
        "audio_path",
        "raw_label",
        "label",
        "leak_size_label",
        "session_id",
        "mic_id",
        *config["metadata_fields"],
    ]

    for raw_label in config["raw_labels"]:
        label_dir = args.raw_dir / raw_label
        if not label_dir.exists():
            continue
        for audio_path in sorted(label_dir.glob("*.wav")):
            relative_audio_path = audio_path.resolve().relative_to(output_parent)
            row = {
                "audio_path": str(relative_audio_path).replace("\\", "/"),
                "raw_label": raw_label,
                "label": label_map.get(raw_label, raw_label),
                "leak_size_label": leak_size_map.get(raw_label, "unknown"),
                "session_id": infer_session_id(audio_path),
                "mic_id": "",
            }
            for metadata_field in config["metadata_fields"]:
                row[metadata_field] = ""
            rows.append(row)

    write_csv(rows, args.output, fieldnames)
    print(f"Wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
