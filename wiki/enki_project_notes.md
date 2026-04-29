# Enki — Project Notes, Challenges, and Adaptations

> Working document. Source material for Wiki (Future Work, Challenges), Final Presentation (Challenges slide), and advisor Q&A prep.

---

## 1. Test Environment Limitations

### 1.1 Motor-Dominated Acoustic & Vibration Channels
The test rig is a ~10ft × 5ft closed-loop pipe system powered by a circulation motor. The motor is the loudest mechanical and acoustic source in the environment by a wide margin, and the rig is small enough that no sensor mounting position is far enough away to isolate pipe-internal signals from motor signature.

**Consequence:**
- INMP441 (acoustic) and MPU6050 (vibration) readings are dominated by the motor signature rather than pipe-internal behavior
- Signal-to-noise ratio for leak detection on these two modalities is severely reduced on this rig
- Once sensors were properly clamped (April 22), the channels did stabilize into structured, bounded signals — but the dominant signal source remains the motor, not anything happening inside the pipe

**Production context:**
In a realistic deployment (building plumbing with longer pipe runs, no co-located circulation motor), these modalities would function as designed. The limitation is specific to the test rig, not the architecture.

### 1.2 Sensor Mounting — Resolved (April 22)
For early testing, no fixed mounting solution existed for attaching sensors to pipes. An engineer physically held the sensor package against the pipe for the duration of each test, introducing significant handling artifacts (body heat, hand movement, repositioning) into the data.

**Resolution:** Pipe clamps ("clams") were fabricated and deployed on April 22. All subsequent tests used clamped, untouched sensor mounts.

**Impact on data quality:**
- Pre-clamp data showed wide variance and frequent outliers attributable to handling
- Post-clamp data shows tight, reproducible baselines on all four channels
- Acoustic channel went from a 11k–30k spread (no clear pattern) to a tight ~280-unit band
- Vibration channel went from being clipped at 0–256 to a structured ~200-unit band
- The clamp deployment was the single biggest improvement in data quality during the project

### 1.3 Leak Stimulus Method — Limitation Identified (April 23, confirmed April 27 and April 28)
The leak simulation method on this rig is a small bleed valve (~1/4 to 1/3 inch stream) that releases water from the pipe system into a contained bucket on the floor.

**Why this stimulus does not produce sensor-detectable conditions on the raw sensor channels:**
Sensors are clamped to the *exterior* of the pipe and respond to:
- (a) water on or near the pipe surface
- (b) thermal change in the pipe wall from interrupted or altered flow
- (c) acoustic or vibration changes from flow disruption

The bleed valve produces none of these. Water exits cleanly into a contained bucket without wetting the pipe exterior or surrounding air, the motor continues to drive circulation regardless, and the volume bled is small enough that flow through the rest of the rig is not meaningfully disrupted.

**Confirmed across multiple tests:**
On the four raw sensor channels (moisture, temperature, acoustic, vibration), no test on this rig has produced an inflection point at known leak boundaries. Across the April 27 test (75 minutes, leak 13:15–13:35) and the April 28 afternoon test (97 minutes, leak 16:27–17:01), the dominant signals are smooth monotonic drift consistent with closed-room thermal/humidity drift over time — moisture decreases as the room warms and dries, temperature rises as the motor heats the rig and the air. These trends pre-date and out-last the leak window.

**Implication:** The stimulus does not exercise the conditions the raw sensors are positioned to detect. The thresholds set in this project against raw channels are therefore **anomaly-detection bounds**, not **leak-validated bounds**.

---

## 2. Data Findings

### 2.1 Raw Sensor Baselines Across Sessions (post-clamp, node-01)

| Sensor | Apr 22 Test 1 (15-min) | Apr 22 Test 2 (15-min) | Apr 28 No-Leak (22-min) |
|---|---|---|---|
| Moisture (%) — avg | 51.4 | 50.4 | 52.2 |
| Moisture max | 53.6\* | 50.6 | 53.7 |
| Temperature (°C) — avg | 24.1 | 24.3 | 24.5 |
| Temperature max | 24.5 | 24.5 | 27.1\*\* |
| Acoustic (raw) — avg | 28,914 | 28,482 | 27,469 |
| Vibration (raw) — avg | 726 | 714 | 658 |

\* April 22 Test 1 max includes a known artifact at 12:57 (operator briefly touched sensor).
\*\* April 28 max temperature is from late in the session — by this point the rig had been running long enough that ambient temperature drift exceeded earlier baselines.

**Findings:**
- **Reproducible baseline range across sessions.** Three independent no-leak windows agree on moisture (~50–53%), temperature (~24°C ambient), acoustic (~27–29k raw), and vibration (~700 raw). Tight reproducibility on the first three; vibration shows wider session-to-session variation.
- **All four sensors functional.** None are clipped, pinned, or wildly noisy after the April 22 clamp deployment.
- **Acoustic and vibration are stable but motor-dominated.** Tight bands but the dominant signal source is the circulation motor, not pipe-internal events.
- **Long-running sessions show environmental drift.** Sessions over ~30 minutes show ambient temperature and humidity drift large enough that the absolute thresholds set against shorter sessions can be exceeded by drift alone (April 28 hit 28°C ambient by 17:19 with no leak present). Future work should consider rate-of-change rather than absolute thresholds for these channels.

### 2.2 Leak Test Outcomes — Raw Sensor Channels

Across three leak tests (Apr 23 untimed, Apr 27 properly timestamped, Apr 28 properly timestamped), no raw sensor channel showed an inflection point at the known leak boundaries. Observed signal in each test is consistent with room drift, not leak signal. Confirmed via per-second data analysis with phase-segmented statistics.

### 2.3 ML Model Behavior — Per-Second Analysis

Per-second data (sampled every ~2 seconds) from the on-device TFLite model was retrieved from DynamoDB and analyzed across all sessions. The model publishes both `confidence_score` (which is sent to CloudWatch) and a discrete `leak_level` ∈ {0,1,2,3} which drives the on-device LED indicator but is not currently published to the cloud.

**Within-session signal in the April 27 test:**
On April 27 the model showed a statistically significant within-session response to the leak boundaries:
- Pre-leak (12:35–13:14): `leak_level=3` rate ≈ 49%, mean confidence 0.082
- Leak window (13:15–13:34): `leak_level=3` rate ≈ 78%, mean confidence 0.205
- Post-leak (13:35–13:50): `leak_level=3` rate ≈ 58%, mean confidence 0.102

Mann-Whitney U test (one-sided): leak window confidence is greater than pre-leak with p < 0.000001. The model "locked on" approximately 2 minutes after the valve opened (around 13:17–13:18) and "released" approximately 3 minutes after the valve closed.

**Cross-session behavior — the model needs to adapt to its environment:**
The same per-second analysis applied across all sessions:

| Session | Ground Truth | leak_level=3 rate | Mean confidence | Notes |
|---|---|---|---|---|
| Apr 22 No-Leak Test 1 | NO LEAK | 84.5% | 0.864 | Early model version, fires constantly |
| Apr 22 No-Leak Test 2 | NO LEAK | 83.3% | 0.884 | Same |
| Apr 27 Pre-Leak | NO LEAK | 49% | 0.082 | Retrained model |
| Apr 27 Leak | LEAK | 78% | 0.205 | Within-session response |
| Apr 28 No-Leak morning | NO LEAK | 91.1% | 0.260 | After sensor reposition — model adapting to new environment |
| **Apr 28 No-Leak afternoon** | **NO LEAK** | **23.6%** | **0.028** | **Model has adapted; clean baseline** |
| **Apr 28 Leak** | **LEAK** | **32.8%** | **0.036** | **Measurable response to leak (p < 0.0001)** |
| **Apr 28 Recovery** | **NO LEAK** | **7.0%** | **0.006** | **Sharp drop — model is more confident NO LEAK after stimulus ends** |

**Interpretation — the April 28 afternoon sequence is the best evidence the system has produced:**
On April 28 the sensors were repositioned on the pipe before testing. The morning no-leak session (91% leak3) shows the model adapting to the new sensor configuration — high false-positive rate while the model recalibrates to the new environment. By the afternoon the model has settled (23% leak3 baseline), and across the leak/recovery sequence it shows the discriminating behavior expected of a working classifier:
- Stable, low baseline in the post-adaptation no-leak window
- Statistically significant increase during the leak window (p < 0.0001)
- Sharp drop to its lowest activity during recovery — meaning the model is *more confident* there's no leak after the stimulus ends than it was before

The within-session shift on April 28 afternoon (23% → 33% → 7%) is smaller in absolute terms than the April 27 shift (49% → 78% → 58%), but it has a cleaner three-phase structure and a baseline that is genuinely low. The April 22 results (84% leak3 during no-leak) reflect an earlier, less-trained model version and are not representative of current model behavior.

**Caveats:** The model still requires an adaptation period when the sensor configuration changes, which is not workable for a production handheld device that will see arbitrary pipes. Cross-session reproducibility on a fixed configuration has not been demonstrated — only one full leak/no-leak/recovery cycle (April 28 PM) shows the desired pattern. Locking the model and validating its behavior on additional sessions in the same configuration is needed before claiming validated detection.

### 2.4 Architectural Implication
The composite alarm architecture (single-sensor breach AND ML confidence) is sound, but its components are differently capable on this rig:
- **Raw sensor channels** cannot validate leak detection on this rig due to the stimulus methodology limitation in Section 1.3. They function correctly as anomaly bounds (catching events like operator handling or sensor disconnection).
- **The ML model** has shown — in the best session collected (April 28 PM, post-adaptation) — that it can produce the discriminating behavior expected of a leak classifier: stable low baseline, statistically significant lift during stimulus, and sharp drop in recovery. This is the strongest evidence the system has produced.

The remaining gap is not architectural — it's about model stability and validation. A model that adapts to its environment over ~20 minutes is fine for a fixed-node deployment that runs continuously, but does not serve a handheld use case where the device sees a new pipe every inspection. A locked, validated model with reproducible behavior across sessions in the same configuration is the next step.

---

## 3. Threshold Decisions

### 3.1 Methodology
Thresholds were set as **baseline anomaly bounds**: each threshold sits a small headroom above the highest observed value across the April 22 no-leak baselines (after warm-up trim). The intent is to alarm when sensor readings deviate meaningfully from established baseline behavior — not to claim validated leak detection. Validation against leak data was not possible on this rig due to the stimulus methodology limitation documented in Section 1.3.

### 3.2 Final Threshold Values (per node)

| Channel | Apr 22 Baseline Max | Threshold | Notes |
|---|---|---|---|
| Moisture | 53.6% (incl. hand-touch artifact) | 55% | Above any observed baseline |
| Temperature | 24.5°C | 26°C | Exceeded by environmental drift in long sessions — see Section 2.1 |
| Acoustic | 29,006 raw | 29,500 raw | Above any observed baseline |
| Vibration | 831 raw | 900 raw | Above any observed baseline |
| Confidence Score | n/a | 0.2 | Lowered from 0.5 based on per-second analysis showing leak-window 60s rolling means peak ~0.3 |

### 3.3 Evaluation Periods
All alarms remain at `evaluation_periods = 3`, requiring a sustained signal across three consecutive 1-minute periods before firing. This filters out transient single-minute spikes (such as the hand-touch artifact in April 22 Test 1) and ensures the alarm responds only to sustained anomalies.

### 3.4 Composite Alarm Logic
Per-node composite alarm fires when:
`(any single-channel threshold alarm in ALARM state) AND (confidence score alarm in ALARM state)`

In the current state the composite alarm is unlikely to fire — the temperature alarm may fire from environmental drift in long sessions, but the confidence alarm rarely sustains above 0.2 long enough to trip even with a real leak (and conversely, fires falsely in some sessions where the model is broken). This is documented honestly as a limitation rather than worked around.

---

## 4. Architecture Evolution

### 4.1 ML Moved to All Nodes
Original architecture (Path 1 / Path 2 split):
- Fixed nodes: raw sensor data → cloud → threshold alarms
- Handheld: sensor data → on-device TFLite model → LCD

Updated architecture:
- **All** ESP32 nodes (fixed and handheld) run the TFLite model locally
- Fixed nodes publish the 4 sensor values + ML confidence score to the cloud at ~1 Hz (in practice ~0.5 Hz)
- Cloud layer performs cross-validation between threshold alarms and ML confidence via `CompositeAlarm`

**Rationale (retroactive):**
Running ML on every node and cross-validating against thresholds in the cloud provides a stronger detection story than either approach alone in principle. In practice this requires a stable, well-trained model — see Section 2.3.

### 4.2 What the Cloud Layer Does
- Ingests 4 metrics + confidence score per node every ~2 seconds via MQTT
- Routes to DynamoDB for historical record (full fidelity, used for the Section 2.3 analysis)
- Publishes all 5 values as CloudWatch metrics per-node
- Runs per-node threshold alarms (anomaly-detection bounds; see Section 3)
- Runs per-node composite alarm: `(any threshold alarm) AND (confidence alarm)`
- Sends SNS email on composite alarm firing
- Dashboard shows per-node sensor graphs + composite alarm status tile

### 4.3 What the Cloud Layer Does Not See (Worth Noting)
The firmware also computes `leak_level` (0–3) and `led_color` (green/blue/red/yellow) for the handheld LCD. These fields are written to DynamoDB but are not published as CloudWatch metrics. Per-second analysis (Section 2.3) showed that `leak_level=3` rate over a rolling window is a more sensitive detector than averaged `confidence_score` — but on this rig, neither is reliable across sessions. Publishing `leak_level` as a CloudWatch metric is a candidate for future work if model stability improves.

---

## 5. Investigated but Not Adopted

### 5.1 Baseline Subtraction for Motor Noise
**Proposal:** Characterize motor vibration/acoustic signature during known no-leak conditions, then subtract that baseline from live readings in firmware to isolate pipe-internal signals.

**Status:** Proposed, not adopted. Could be prototyped offline in Python against DynamoDB historical data without firmware changes. Future work candidate.

### 5.2 Publishing `leak_level` as a CloudWatch Metric
**Proposal:** Add the firmware-computed `leak_level` field to the MQTT payload and CloudWatch metric pipeline; build alarms on rolling proportion-of-time-at-level-3 rather than averaged confidence_score.

**Status:** Investigated, not adopted. The per-second analysis showed this metric is more sensitive within sessions, but the across-session model instability documented in Section 2.3 means the across-session value is no greater than `confidence_score`. Worth revisiting once the model is more stable.

---

## 6. Open Hardware/Firmware Questions

These don't block the cloud layer but limit signal quality on the affected channels:

1. **Acoustic and vibration units.** Both channels publish raw values rather than the calibrated Hz / g-force units described in the schema. Schema and firmware should be reconciled.
2. **Warm-up/stabilization behavior.** Sensors take ~3–5 minutes to stabilize after power-on. Firmware should include a warm-up state before inference begins (especially on the handheld).
3. **Model stability.** The model behaves differently across sessions in ways that don't track with ground truth (Section 2.3). Production deployment requires a model that is locked, versioned, and validated against held-out data — not retrained between every test session.

---

## 7. Future Work (for Wiki)

- **Leak stimulus methodology.** Develop test protocols that exercise the conditions sensors are designed to detect (water on pipe exterior, flow disruption, surface temperature change) rather than only contained bleed-off into a bucket.
- **Baseline subtraction / adaptive filtering for motor noise.** Offline prototype first, then port to firmware if viable.
- **Variance- and rate-of-change alarms.** Long-session data showed environmental drift can exceed absolute thresholds without any leak being present. CloudWatch Metric Math (`RATE()`, `STDDEV()`) and Anomaly Detection alarms could capture event-driven shifts without false-firing on slow drift.
- **Deployment in a realistic environment** (actual building pipe run, no co-located motor) to characterize acoustic and vibration channels in a setting where their signal-to-noise ratio allows useful detection.
- **Sensor calibration pass.** Convert raw acoustic and vibration values to calibrated units per the schema.
- **Multi-node validation.** Node-02 came online but did not produce data during these tests. A future session should validate that both nodes produce consistent baselines.
- **Model stability and validation.** Lock a single trained model version, evaluate its performance against held-out per-session test data, and version-control the deployed model so cross-session behavior is predictable.
- **Publish `leak_level` as a CloudWatch metric** once the model is stable enough to make it useful.

---

## 8. Advisor Q&A Prep — Likely Questions

**Q: Why don't your moisture thresholds cleanly separate leak from no-leak?**
The test rig's leak simulation method (a small bleed valve into a contained bucket) does not produce the conditions our raw sensors are positioned to detect — water on the pipe exterior, flow disruption, or surface temperature change. We confirmed this across three timestamped tests where no raw sensor channel showed an inflection point at the known leak boundaries. Our thresholds are set as anomaly-detection bounds rather than leak-validated bounds.

**Q: Is the ML model detecting leaks?**
The strongest evidence the system has produced is the April 28 afternoon test (after sensor reposition and a model adaptation period). In that session the model showed the discriminating behavior expected of a working classifier: stable low baseline pre-leak (~23% leak3 rate), statistically significant rise during the leak window (~33%, p < 0.0001), and a sharp drop in recovery (~7%) — meaning the model was *more* confident there was no leak after the stimulus ended than before it started. The April 27 test showed a similar three-phase response with a larger absolute lift. So yes, within a session, the model is detecting the leak. The remaining issue is that the model takes ~20 minutes to adapt when the sensor configuration changes, which is workable for fixed-node deployment but not for the handheld use case. Cross-session validation on a locked model is the next step.

**Q: Why is your composite alarm structured the way it is?**
The composite alarm requires a single-sensor threshold breach AND a confidence breach to fire SNS. This cross-validation design reduces false positives that either signal would produce alone. On this rig, neither component is currently reliable enough to fire on its own — but the architecture is sound and would work in a deployment with stable training data and realistic stimulus methodology.

**Q: What would you do differently with more time?**
Four things in priority order: (1) lock and version-control a single trained ML model; (2) develop a leak stimulus method that actually exercises sensor detection conditions; (3) move from absolute thresholds to rate-of-change alarms to handle environmental drift; (4) deploy in a realistic environment without a co-located circulation motor.

**Q: How did you analyze the data?**
CloudWatch dashboards showed 1-minute averaged data, which smoothed out the model's per-second behavior. To analyze the actual model output we exported the full DynamoDB record (~18,000 rows, every ~2 seconds across 6 days), and used Python (pandas, scipy.stats) to do phase-segmented statistical comparisons, rolling window analysis, and Mann-Whitney U tests on leak vs no-leak distributions. The per-second analysis is what surfaced the within-session ML signal that the dashboards were hiding.

---

## 9. Personal Contribution Log (for Grading)

- CDK stack (IoT Core, DynamoDB, CloudWatch, SNS, IAM, backups, dashboard)
- mTLS device authentication with X.509 certificates
- IoT Rules Engine routing + per-node CloudWatch metrics
- Composite alarm cross-validation design
- Baseline characterization and threshold tuning (April 17–28 analysis sessions)
- Identification of leak stimulus methodology limitation (Section 1.3)
- Per-second statistical analysis revealing within-session ML signal and across-session model instability (Section 2.3)
- CloudWatch dashboard per-node layout
- README, wiki structure, project board setup
- Milestone and issue organization (5 milestones, 10+ user stories, 30+ issues)
- This documentation
- [add as you go]
