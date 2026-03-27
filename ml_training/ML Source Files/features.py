from __future__ import annotations

import numpy as np


def window_samples(config: dict) -> int:
    return int(config["window_samples"])


def feature_column_names(config: dict) -> list[str]:
    return list(config["feature_columns"])


def pad_or_trim_audio(audio: np.ndarray, target_samples: int) -> np.ndarray:
    if len(audio) > target_samples:
        return audio[:target_samples].astype(np.float32)
    if len(audio) < target_samples:
        padded = np.zeros(target_samples, dtype=np.float32)
        padded[: len(audio)] = audio
        return padded
    return audio.astype(np.float32)


def to_int16_feature_domain(audio: np.ndarray, config: dict) -> np.ndarray:
    target = window_samples(config)
    prepared = pad_or_trim_audio(audio, target)
    scaled = np.clip(prepared * 32768.0, -32768.0, 32767.0)
    return scaled.astype(np.int16)


def compute_rms(audio_i16: np.ndarray) -> float:
    values = audio_i16.astype(np.float32)
    return float(np.sqrt(np.mean(np.square(values)) + 1e-12))


def compute_zero_crossing_rate(audio_i16: np.ndarray) -> float:
    if len(audio_i16) < 2:
        return 0.0
    signs = audio_i16 >= 0
    crossings = np.logical_xor(signs[1:], signs[:-1]).sum()
    return float(crossings / max(len(audio_i16) - 1, 1))


def compute_spectral_features(audio_i16: np.ndarray, config: dict) -> dict[str, float]:
    values = audio_i16.astype(np.float32)
    spectrum = np.fft.rfft(values)
    magnitudes = np.abs(spectrum)
    freqs = np.fft.rfftfreq(len(values), d=1.0 / float(config["sample_rate"]))

    peak_index = int(np.argmax(magnitudes))
    peak_frequency = float(freqs[peak_index])

    magnitude_sum = float(np.sum(magnitudes))
    if magnitude_sum > 0.0:
        centroid = float(np.sum(freqs * magnitudes) / magnitude_sum)
    else:
        centroid = 0.0

    bands = config["spectral_bands"]
    power = np.square(magnitudes)
    low_band = float(np.sum(power[freqs < float(bands["low_band_max_hz"])]))
    mid_mask = (freqs >= float(bands["low_band_max_hz"])) & (freqs < float(bands["mid_band_max_hz"]))
    high_mask = (freqs >= float(bands["mid_band_max_hz"])) & (freqs <= float(bands["high_band_max_hz"]))
    mid_band = float(np.sum(power[mid_mask]))
    high_band = float(np.sum(power[high_mask]))

    return {
        "peak_frequency_hz": peak_frequency,
        "spectral_centroid_hz": centroid,
        "low_band_energy": low_band,
        "mid_band_energy": mid_band,
        "high_band_energy": high_band,
    }


def _safe_metadata_float(metadata: dict | None, key: str) -> float:
    if metadata is None:
        return 0.0
    value = metadata.get(key, 0.0)
    if value is None:
        return 0.0
    if isinstance(value, str) and not value.strip():
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def build_feature_record(audio: np.ndarray, config: dict, metadata: dict | None = None) -> dict[str, float]:
    audio_i16 = to_int16_feature_domain(audio, config)
    spectral = compute_spectral_features(audio_i16, config)

    record = {
        "rms": compute_rms(audio_i16),
        "peak_frequency_hz": spectral["peak_frequency_hz"],
        "spectral_centroid_hz": spectral["spectral_centroid_hz"],
        "low_band_energy": spectral["low_band_energy"],
        "mid_band_energy": spectral["mid_band_energy"],
        "high_band_energy": spectral["high_band_energy"],
        "zero_crossing_rate": compute_zero_crossing_rate(audio_i16),
        "temperature_c": _safe_metadata_float(metadata, "temperature_c"),
        "humidity_pct": _safe_metadata_float(metadata, "humidity_pct"),
        "vibration_magnitude": _safe_metadata_float(metadata, "vibration_magnitude"),
        "vibration_mean": _safe_metadata_float(metadata, "vibration_mean"),
        "vibration_variance": _safe_metadata_float(metadata, "vibration_variance"),
        "vibration_trend": _safe_metadata_float(metadata, "vibration_trend"),
    }
    return record


def build_feature_vector(audio: np.ndarray, config: dict, metadata: dict | None = None) -> np.ndarray:
    record = build_feature_record(audio, config, metadata)
    return np.asarray([record[name] for name in feature_column_names(config)], dtype=np.float32)
