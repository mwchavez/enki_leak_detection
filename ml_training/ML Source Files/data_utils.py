from __future__ import annotations

import csv
import json
import wave
from pathlib import Path

import numpy as np


def load_config(config_path: str | Path) -> dict:
    with Path(config_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_wav_mono(audio_path: str | Path, target_sample_rate: int) -> np.ndarray:
    audio_path = Path(audio_path)
    with wave.open(str(audio_path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
        raw = wav_file.readframes(frames)

    dtype_map = {1: np.int8, 2: np.int16, 4: np.int32}
    if sample_width not in dtype_map:
        raise ValueError(f"Unsupported WAV sample width {sample_width} in {audio_path}")

    audio = np.frombuffer(raw, dtype=dtype_map[sample_width]).astype(np.float32)
    if channels > 1:
        audio = audio.reshape(-1, channels).mean(axis=1)

    scale = float(2 ** (8 * sample_width - 1))
    audio /= scale

    if sample_rate != target_sample_rate:
        audio = resample_audio(audio, sample_rate, target_sample_rate)

    return audio.astype(np.float32)


def resample_audio(audio: np.ndarray, source_rate: int, target_rate: int) -> np.ndarray:
    if source_rate == target_rate:
        return audio.astype(np.float32)

    duration = len(audio) / float(source_rate)
    source_times = np.linspace(0.0, duration, num=len(audio), endpoint=False)
    target_length = int(round(duration * target_rate))
    target_times = np.linspace(0.0, duration, num=target_length, endpoint=False)
    return np.interp(target_times, source_times, audio).astype(np.float32)


def write_wav_mono(audio_path: str | Path, audio: np.ndarray, sample_rate: int) -> None:
    audio_path = Path(audio_path)
    ensure_parent(audio_path)
    clipped = np.clip(audio, -1.0, 1.0)
    pcm = (clipped * 32767.0).astype(np.int16)

    with wave.open(str(audio_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm.tobytes())


def write_csv(rows: list[dict], output_path: str | Path, fieldnames: list[str]) -> None:
    output_path = Path(output_path)
    ensure_parent(output_path)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
