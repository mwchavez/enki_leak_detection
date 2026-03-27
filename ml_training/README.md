# Dataset Layout

This folder holds the audio data, the manifest, and the extracted features used by the training pipeline.

## Folder Structure

- `ml/data/raw/<raw_label>/`
  Raw `.wav` files grouped by class name
- `ml/data/manifest.csv`
  One row per recording with labels and metadata
- `ml/data/features/features.csv`
  Extracted feature table used for training

## Supported Raw Labels

The current folder labels are:

- `no_leak`
- `small_leak`
- `medium_leak`
- `large_leak`
- `leak`

For training, the current deployed model maps them into:

- `no_leak`
- `leak`

So `small_leak`, `medium_leak`, and `large_leak` are grouped into the leak class in the current version.

## Manifest Fields

The manifest can include:

- `audio_path`
- `raw_label`
- `label`
- `leak_size_label`
- `session_id`
- `mic_id`
- `temperature_c`
- `humidity_pct`
- `pressure_hpa`
- `gas_resistance_ohm`
- `distance_cm`
- `vibration_magnitude`
- `vibration_mean`
- `vibration_variance`
- `vibration_trend`
- `notes`

## Features Used by the Current Model

The current deployable model uses:

- `rms`
- `peak_frequency_hz`
- `spectral_centroid_hz`
- `low_band_energy`
- `mid_band_energy`
- `high_band_energy`
- `zero_crossing_rate`
- `temperature_c`
- `humidity_pct`
- `vibration_magnitude`
- `vibration_mean`
- `vibration_variance`
- `vibration_trend`

## Current Rules

- Split by `session_id`, not just by random clips.
- Keep `no_leak` and `leak` sessions separated across train, validation, and test.
- Keep logging extra metadata even if the current model does not use all of it yet.
- Synthetic audio is useful for testing the pipeline, but real pipe recordings are still needed for final model validation.
