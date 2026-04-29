## 1. Data Separability Findings

### 1.1 Controlled Experiment Summary
Comparison of baseline ("no leak") and stimulus ("leak") windows on node-01, same conditions, same operator, same handling pattern.

| Sensor | No-Leak (Min/Max/Avg) | Leak (Min/Max/Avg) | Observation |
|---|---|---|---|
| Moisture (%) | 45.2 / 51.8 / 48.7 | 38.9 / 55.9 / 47.1 | Means nearly identical; leak window has wider variance in both directions |
| Temperature (°C) | 28.3 / 30.5 / 29.2 | 28.0 / 31.9 / 30.3 | Small but consistent upward shift in leak window (~1°C) |
| Acoustic (raw) | 11,031 / 27,031 / 17,407 | 10,289 / 30,931 / 19,277 | Wide overlap; motor-dominated; units inconsistent with Hz schema |
| Vibration (raw) | 0 / 256 / 7.25 | 0 / 256 / 5.56 | Values clipped at 0–256 range; leak average *lower* than baseline — inconsistent with expected physics |

### 1.2 Key Findings
- **No single sensor cleanly separates leak from no-leak on this rig.** All four modalities show significant overlap between the two conditions.
- **Temperature is the most physically coherent signal** — a ~1°C upward shift aligns with the original proposal's "temperature change" detection idea.
- **Moisture variance increases during leaks** even when the mean does not shift significantly — suggests detection should consider spread, not just absolute level.
- **Vibration data appears to be clipped or miscalibrated** (0–256 range, leak mean lower than baseline). Needs firmware investigation before it can be used.
- **Acoustic data scale does not match schema** — publishing raw values in the 10k–30k range while schema and alarm thresholds were designed around Hz (alarm at 500). Either the schema or the firmware needs to be reconciled.

### 1.3 Architectural Implication
**Single-sensor thresholding alone will not reliably detect leaks in this environment.** This is not a tuning problem — it is a fundamental limit of the data the rig can produce. The project's multi-modal fusion architecture (composite alarm + ML confidence score) is the actual detection mechanism. Single-sensor thresholds function as corroborating evidence and per-channel monitoring, not as primary detectors.

---

## 2. Architecture Evolution

### 2.1 ML Moved to All Nodes
Original architecture (Path 1 / Path 2 split):
- Fixed nodes: raw sensor data → cloud → threshold alarms
- Handheld: sensor data → on-device TFLite model → LCD

Updated architecture:
- **All** ESP32 nodes (fixed and handheld) run the TFLite model locally
- Fixed nodes publish the 4 sensor values + ML confidence score to the cloud at ~1 Hz
- Cloud layer now performs cross-validation between threshold alarms and ML confidence via `CompositeAlarm`

**Rationale (retroactive):**
Running ML on every node and cross-validating against thresholds in the cloud provides a better detection story than either approach alone. It also justifies keeping both systems — thresholds are debuggable and fast; ML captures multi-modal correlations that thresholds cannot.

### What the Cloud Layer Does Now
- Ingests 4 metrics + confidence score per node per second via MQTT
- Routes to DynamoDB for historical record
- Publishes all 5 values as CloudWatch metrics per-node
- Runs per-node threshold alarms (monitoring-grade, not detection-grade given rig limits)
- Runs per-node composite alarm: `(any threshold alarm) AND (confidence alarm)`
- Sends SNS email on composite alarm firing
- Dashboard shows per-node sensor graphs + composite alarm status tile

---

## 3. Open Hardware/Firmware Questions

These are not cloud-layer problems but they block meaningful threshold tuning and ML signal quality:

1. **Vibration sensor output range.** Why is data clipped at 0–256? Is the firmware publishing raw ADC values instead of calibrated g-force? Why does the leak window average read *lower* than baseline?
2. **Acoustic sensor output units.** Schema says Hz; values come in at 10k–30k. Is this a dominant-frequency reading, a raw FFT magnitude, a raw I2S sample value, or something else? Alarm threshold was designed for the schema and is now meaningless.
3. **Sensor mounting fixtures.** No clamps or fixed mounts for pipe attachment. Every data collection session requires an engineer to hold the sensor package manually.
4. **Warm-up/stabilization behavior.** Humidity sensor takes ~3 minutes to stabilize after power-on. Handheld device firmware should include a warm-up state before inference begins.

---
  
