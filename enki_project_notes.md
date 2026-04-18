# Enki — Project Notes, Challenges, and Adaptations

> Working document. Source material for Wiki (Future Work, Challenges), Final Presentation (Challenges slide), and advisor Q&A prep.

---

## 1. Test Environment Limitations

### 1.1 Motor-Dominated Acoustic & Vibration Channels
The test rig is a ~10ft × 5ft closed-loop pipe system powered by a circulation motor. The motor is the loudest mechanical and acoustic source in the environment by a wide margin, and the rig is small enough that no sensor mounting position is far enough away to isolate pipe-internal signals from motor signature.

**Consequence:**
- INMP441 (acoustic) and MPU6050 (vibration) readings are dominated by motor signal rather than pipe behavior
- Signal-to-noise ratio for leak detection on these two modalities is effectively zero on this rig
- Separation between leak and no-leak conditions on these channels is not achievable with the current environment

**Production context:**
In a realistic deployment (building plumbing with longer pipe runs, no co-located circulation motor), these modalities would function as designed. The limitation is specific to the test rig, not the architecture.

### 1.2 Sensor Mounting Is Unresolved
There is no fixed mounting solution for attaching sensors to the pipes. During data collection, an engineer physically holds the sensor package against the pipe for the duration of the test window (~20 minutes per session).

**Consequence:**
- All collected data includes human handling artifacts (body heat, hand movement, breathing, repositioning)
- Baseline and leak windows both contain handling noise, which complicates signal extraction
- Clean, long-duration baseline data is not currently collectable
- Controlled repeatability is compromised — each session's handling profile is slightly different

**Mitigation:**
Handling is present in both baseline and leak windows, which partially controls for it as a confounding variable. However, this increases variance in both conditions and reduces the separability of leak signal from baseline noise.

**Needed:**
Pipe clamp fixtures for permanent sensor mounting. Design has not been completed.

---

## 2. Data Separability Findings

### 2.1 Controlled Experiment Summary
Comparison of baseline ("no leak") and stimulus ("leak") windows on node-01, same conditions, same operator, same handling pattern.

| Sensor | No-Leak (Min/Max/Avg) | Leak (Min/Max/Avg) | Observation |
|---|---|---|---|
| Moisture (%) | 45.2 / 51.8 / 48.7 | 38.9 / 55.9 / 47.1 | Means nearly identical; leak window has wider variance in both directions |
| Temperature (°C) | 28.3 / 30.5 / 29.2 | 28.0 / 31.9 / 30.3 | Small but consistent upward shift in leak window (~1°C) |
| Acoustic (raw) | 11,031 / 27,031 / 17,407 | 10,289 / 30,931 / 19,277 | Wide overlap; motor-dominated; units inconsistent with Hz schema |
| Vibration (raw) | 0 / 256 / 7.25 | 0 / 256 / 5.56 | Values clipped at 0–256 range; leak average *lower* than baseline — inconsistent with expected physics |

### 2.2 Key Findings
- **No single sensor cleanly separates leak from no-leak on this rig.** All four modalities show significant overlap between the two conditions.
- **Temperature is the most physically coherent signal** — a ~1°C upward shift aligns with the original proposal's "temperature change" detection idea.
- **Moisture variance increases during leaks** even when the mean does not shift significantly — suggests detection should consider spread, not just absolute level.
- **Vibration data appears to be clipped or miscalibrated** (0–256 range, leak mean lower than baseline). Needs firmware investigation before it can be used.
- **Acoustic data scale does not match schema** — publishing raw values in the 10k–30k range while schema and alarm thresholds were designed around Hz (alarm at 500). Either the schema or the firmware needs to be reconciled.

### 2.3 Architectural Implication
**Single-sensor thresholding alone will not reliably detect leaks in this environment.** This is not a tuning problem — it is a fundamental limit of the data the rig can produce. The project's multi-modal fusion architecture (composite alarm + ML confidence score) is the actual detection mechanism. Single-sensor thresholds function as corroborating evidence and per-channel monitoring, not as primary detectors.

---

## 3. Architecture Evolution

### 3.1 ML Moved to All Nodes
Original architecture (Path 1 / Path 2 split):
- Fixed nodes: raw sensor data → cloud → threshold alarms
- Handheld: sensor data → on-device TFLite model → LCD

Updated architecture:
- **All** ESP32 nodes (fixed and handheld) run the TFLite model locally
- Fixed nodes publish the 4 sensor values + ML confidence score to the cloud at ~1 Hz
- Cloud layer now performs cross-validation between threshold alarms and ML confidence via `CompositeAlarm`

**Rationale (retroactive):**
Running ML on every node and cross-validating against thresholds in the cloud provides a better detection story than either approach alone. It also justifies keeping both systems — thresholds are debuggable and fast; ML captures multi-modal correlations that thresholds cannot.

**Process note:**
This change was made without full team consensus. Going forward, architectural changes that affect the cloud layer should include the cloud lead in the decision.

### 3.2 What the Cloud Layer Does Now
- Ingests 4 metrics + confidence score per node per second via MQTT
- Routes to DynamoDB for historical record
- Publishes all 5 values as CloudWatch metrics per-node
- Runs per-node threshold alarms (monitoring-grade, not detection-grade given rig limits)
- Runs per-node composite alarm: `(any threshold alarm) AND (confidence alarm)`
- Sends SNS email on composite alarm firing
- Dashboard shows per-node sensor graphs + composite alarm status tile

---

## 4. Investigated but Not Adopted

### 4.1 Baseline Subtraction for Motor Noise
**Proposal:** Characterize motor vibration/acoustic signature during known no-leak conditions, then subtract that baseline from live readings in firmware to isolate pipe-internal signals.

**Status:** Proposed to team, not adopted. Merits further exploration.

**Why it's worth investigating:**
- Directly addresses the single biggest limit of the test rig
- Standard signal-processing practice in vibration analysis
- Could be prototyped offline in Python against DynamoDB historical data without firmware changes

**Future work candidate.**

---

## 5. Open Hardware/Firmware Questions

These are not cloud-layer problems but they block meaningful threshold tuning and ML signal quality:

1. **Vibration sensor output range.** Why is data clipped at 0–256? Is the firmware publishing raw ADC values instead of calibrated g-force? Why does the leak window average read *lower* than baseline?
2. **Acoustic sensor output units.** Schema says Hz; values come in at 10k–30k. Is this a dominant-frequency reading, a raw FFT magnitude, a raw I2S sample value, or something else? Alarm threshold was designed for the schema and is now meaningless.
3. **Sensor mounting fixtures.** No clamps or fixed mounts for pipe attachment. Every data collection session requires an engineer to hold the sensor package manually.
4. **Warm-up/stabilization behavior.** Humidity sensor takes ~3 minutes to stabilize after power-on. Handheld device firmware should include a warm-up state before inference begins.

---

## 6. Future Work (for Wiki)

- **Redesign pipe mounting solution.** Clamp-based fixtures that permanently attach sensors to pipes, eliminating handling noise from data collection.
- **Baseline subtraction / adaptive filtering for motor noise.** Offline prototype first, then port to firmware if viable.
- **Move beyond fixed thresholds to rate-of-change and variance-based alarming.** Moisture data shows that *variance* shifts during leaks even when *mean* does not — CloudWatch Metric Math (`RATE()`, `STDDEV()`) or Anomaly Detection alarms could capture this.
- **Deployment in a realistic environment** (actual building pipe run, no co-located motor) to characterize acoustic/vibration channels in a setting where their signal-to-noise ratio allows useful detection.
- **Sensor calibration pass.** Resolve vibration clipping and acoustic unit/scale questions before relying on these channels for detection.
- **Controlled remote-trigger leak test.** Introduce the leak stimulus without a human handler present, to get a clean "untouched baseline vs untouched leak" comparison.

---

## 7. Advisor Q&A Prep — Likely Questions

**Q: Why don't your moisture thresholds cleanly separate leak from no-leak?**
The test rig constrains baseline quality in two ways: the motor dominates acoustic/vibration channels, and there's no fixed sensor mounting so data collection includes human handling noise. On this specific rig, no single-sensor threshold achieves clean separation. The system was designed around multi-modal fusion specifically to handle cases where no single channel is reliable — the composite alarm combining ML confidence with threshold signals is the actual detection mechanism.

**Q: Why is ML needed if thresholds could work?**
Thresholds work when "normal" is fixed and well-characterized. They break down when (a) normal is contextual, (b) the meaningful signal is a cross-sensor correlation that no single channel captures, or (c) the device has no baseline to threshold against. The handheld device has no baseline — a technician walks up to an arbitrary pipe in an arbitrary building — so it *must* be model-driven. Extending ML to the fixed nodes as well provides cross-validation between two independent detection paths.

**Q: Why are your acoustic/vibration thresholds set where they are?**
Those thresholds are placeholders. The motor-dominated signal on this rig means those channels cannot produce useful single-sensor detection. They're retained in the dashboard as monitoring metrics, not as detection triggers. The composite alarm doesn't rely on them firing.

**Q: What would you do differently with more time?**
Three things: solve the physical sensor mounting problem so data collection doesn't require a human handler; prototype baseline subtraction for motor noise; and collect data in a realistic environment (building pipe run) where acoustic and vibration channels would actually function.

---

## 8. Personal Contribution Log (for Grading)

Keep this updated — the practicum grading formula rewards documented individual contributions.

- CDK stack (IoT Core, DynamoDB, CloudWatch, SNS, IAM, backups, dashboard)
- mTLS device authentication with X.509 certificates
- IoT Rules Engine routing + per-node CloudWatch metrics
- Composite alarm cross-validation design
- Threshold investigation and data analysis (this document)
- CloudWatch dashboard per-node layout
- README, wiki structure, project board setup
- Milestone and issue organization (5 milestones, 10+ user stories, 30+ issues)
- [add as you go]

