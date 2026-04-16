from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_utils import ensure_parent, load_config, read_wav_mono


def pick_default_examples(config: dict) -> list[Path]:
    raw_dir = ROOT / "data" / "raw"
    selected: list[Path] = []
    for raw_label in config["raw_labels"]:
        if raw_label == "leak":
            continue
        match = sorted((raw_dir / raw_label).glob("*.wav"))
        if match:
            selected.append(match[0])
    return selected


def make_safe_name(audio_path: Path) -> str:
    return audio_path.stem.replace(" ", "_")


def build_plot(audio: np.ndarray, sample_rate: int, audio_path: Path, output_path: Path) -> None:
    duration = len(audio) / float(sample_rate)
    times = np.arange(len(audio), dtype=np.float32) / float(sample_rate)
    rms = float(np.sqrt(np.mean(np.square(audio)))) if len(audio) else 0.0

    nfft = min(256, max(32, 2 ** int(np.floor(np.log2(max(len(audio), 32))))))
    noverlap = nfft // 2

    fig, axes = plt.subplots(2, 1, figsize=(10, 6), constrained_layout=True)

    axes[0].plot(times, audio, linewidth=1.0, color="#1f4e79")
    axes[0].set_title(f"Waveform: {audio_path.name}")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(alpha=0.25)
    axes[0].text(
        0.01,
        0.95,
        f"Duration: {duration:.4f} s\nSample Rate: {sample_rate} Hz\nRMS: {rms:.4f}",
        transform=axes[0].transAxes,
        va="top",
        ha="left",
        bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "#cccccc"},
    )

    _, _, _, im = axes[1].specgram(
        audio,
        NFFT=nfft,
        Fs=sample_rate,
        noverlap=noverlap,
        cmap="viridis",
    )
    axes[1].set_title("Spectrogram")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Frequency (Hz)")
    fig.colorbar(im, ax=axes[1], label="Intensity (dB)")

    ensure_parent(output_path)
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create waveform and spectrogram PNGs for WAV audio files."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "configs" / "experiment.json",
        help="Path to experiment configuration.",
    )
    parser.add_argument(
        "--audio",
        type=Path,
        nargs="*",
        default=None,
        help="Optional WAV file paths. If omitted, one default example per class is used.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "outputs" / "visualizations",
        help="Directory where PNG files will be saved.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    sample_rate = int(config["sample_rate"])

    if args.audio:
        audio_paths = [Path(path) for path in args.audio]
    else:
        audio_paths = pick_default_examples(config)

    if not audio_paths:
        raise FileNotFoundError("No WAV files were found to visualize.")

    for audio_path in audio_paths:
        audio = read_wav_mono(audio_path, sample_rate)
        output_path = args.output_dir / f"{make_safe_name(audio_path)}.png"
        build_plot(audio, sample_rate, audio_path, output_path)
        print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
