from __future__ import annotations

import numpy as np


def lowpass_noise(rng: np.random.Generator, count: int, scale: float) -> np.ndarray:
    noise = rng.normal(0.0, scale, count)
    kernel = np.ones(16, dtype=np.float32) / 16.0
    return np.convolve(noise, kernel, mode="same").astype(np.float32)


def band_noise(
    rng: np.random.Generator,
    count: int,
    sample_rate: int,
    low_hz: float,
    high_hz: float,
    scale: float,
) -> np.ndarray:
    white = rng.normal(0.0, 1.0, count)
    spectrum = np.fft.rfft(white)
    freqs = np.fft.rfftfreq(count, d=1.0 / sample_rate)
    mask = (freqs >= low_hz) & (freqs <= high_hz)
    spectrum *= mask
    filtered = np.fft.irfft(spectrum, n=count)
    filtered /= np.max(np.abs(filtered)) + 1e-8
    return (filtered * scale).astype(np.float32)


def synthesize_clip(raw_label: str, sample_rate: int, sample_count: int, rng: np.random.Generator) -> np.ndarray:
    t = np.arange(sample_count, dtype=np.float32) / sample_rate

    ambient = 0.02 * np.sin(2.0 * np.pi * 60.0 * t)
    ambient += 0.01 * np.sin(2.0 * np.pi * 180.0 * t)
    ambient += lowpass_noise(rng, sample_count, 0.015)

    if raw_label == "no_leak":
        signal = ambient
    elif raw_label == "small_leak":
        signal = ambient + band_noise(rng, sample_count, sample_rate, 1500.0, 3000.0, 0.10)
    elif raw_label == "medium_leak":
        signal = ambient + band_noise(rng, sample_count, sample_rate, 1000.0, 4000.0, 0.18)
        signal += 0.02 * np.sin(2.0 * np.pi * 450.0 * t)
    elif raw_label in {"large_leak", "leak"}:
        signal = ambient + band_noise(rng, sample_count, sample_rate, 700.0, 5200.0, 0.30)
        signal += 0.03 * np.sin(2.0 * np.pi * 250.0 * t)
        signal += 0.02 * np.sin(2.0 * np.pi * 800.0 * t)
    else:
        raise ValueError(f"Unknown raw label {raw_label}")

    signal += rng.normal(0.0, 0.005, sample_count)
    signal /= np.max(np.abs(signal)) + 1e-8
    return signal.astype(np.float32)
