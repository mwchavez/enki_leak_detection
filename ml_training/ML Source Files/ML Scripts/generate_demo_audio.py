from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_utils import load_config, write_wav_mono
from synthetic_audio import synthesize_clip


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate audible synthetic demo WAV files.")
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "configs" / "experiment.json",
        help="Path to experiment configuration.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "data" / "demo_audio",
        help="Directory where longer demo WAV files will be created.",
    )
    parser.add_argument(
        "--duration-seconds",
        type=float,
        default=3.0,
        help="Length of each demo WAV file in seconds.",
    )
    parser.add_argument(
        "--samples-per-class",
        type=int,
        default=1,
        help="Number of audible demo files to create per raw label.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    sample_rate = int(config["sample_rate"])
    sample_count = int(round(sample_rate * args.duration_seconds))
    rng = np.random.default_rng(int(config["training"]["random_seed"]) + 1000)

    total = 0
    for raw_label in config["raw_labels"]:
        if raw_label == "leak":
            continue
        for index in range(args.samples_per_class):
            audio = synthesize_clip(raw_label, sample_rate, sample_count, rng)
            if args.samples_per_class == 1:
                filename = f"demo_{raw_label}.wav"
            else:
                filename = f"demo_{raw_label}_{index:03d}.wav"
            output_path = args.output_dir / raw_label / filename
            write_wav_mono(output_path, audio, sample_rate)
            total += 1

    print(f"Generated {total} audible demo clips in {args.output_dir}")


if __name__ == "__main__":
    main()
