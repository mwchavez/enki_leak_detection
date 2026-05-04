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

### 1.3 Leak Stimulus Method — Limitation Identified (April 23, confirmed April 27, 28, 29, and 30)
The leak simulation method on this rig is a small bleed valve (~1/4 to 1/3 inch stream) that releases water from the pipe system into a contained bucket on the floor.

**Why this stimulus does not produce sensor-detectable conditions on the raw sensor channels:**
Sensors are clamped to the *exterior* of the pipe and respond to:
- (a) water on or near the pipe surface
- (b) thermal change in the pipe wall from interrupted or altered flow
- (c) acoustic or vibration changes from flow disruption

The bleed valve produces none of these. Water exits cleanly into a contained bucket without wetting the pipe exterior or surrounding air, the motor continues to drive circulation regardless, and the volume bled is small enough that flow through the rest of the rig is not meaningfully disrupted.

**Confirmed across multiple tests:**
On the four raw sensor channels (moisture, temperature, acoustic, vibration), the dominant signals during leak windows are smooth monotonic drift consistent with closed-room thermal/humidity drift over time — moisture decreases as the room warms and dries, temperature rises as the motor heats the rig and the air. These trends pre-date and out-last the leak window. This pattern was observed across the April 27 test (75 min), April 28 afternoon test (97 min), and the April 29 and April 30 tests on different pipe configurations.

**Important caveat from the April 30 morning test (see Section 2.5):**
On April 30, both nodes did show statistically significant moisture and temperature shifts during the leak window (p < 0.000001 each), with both nodes moving in the same direction by similar magnitudes. However, the *direction* of those shifts (moisture down, temperature up) is consistent with the same room-drift pattern observed in no-leak sessions — meaning the shifts cannot be unambiguously attributed to the leak stimulus rather than to time elapsed during the test. A controlled before/after no-leak comparison of equivalent duration would be needed to separate leak signal from drift.

**Implication:** The stimulus does not unambiguously exercise the conditions the raw sensors are positioned to detect. The thresholds set in this project against raw channels are therefore **anomaly-detection bounds**, not **leak-validated bounds**.

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

**Cross-session behavior — model is unstable across sessions in ways not yet fully understood:**
The same per-second analysis applied across all sessions:

| Session | Ground Truth | leak_level=3 rate | Mean confidence | Notes |
|---|---|---|---|---|
| Apr 22 No-Leak Test 1 | NO LEAK | 84.5% | 0.864 | Early model version, fires constantly |
| Apr 22 No-Leak Test 2 | NO LEAK | 83.3% | 0.884 | Same |
| Apr 27 Pre-Leak | NO LEAK | 49% | 0.082 | Retrained model |
| Apr 27 Leak | LEAK | 78% | 0.205 | Within-session response (p < 0.000001) |
| Apr 28 No-Leak morning | NO LEAK | 91.1% | 0.260 | After sensor reposition — assumed adaptation |
| **Apr 28 No-Leak afternoon** | NO LEAK | 23.6% | 0.028 | Clean baseline |
| **Apr 28 Leak** | LEAK | 32.8% | 0.036 | Measurable response (p < 0.0001) |
| **Apr 28 Recovery** | NO LEAK | 7.0% | 0.006 | Sharp drop — model is more confident NO LEAK after stimulus ends |
| Apr 29 No-Leak (different pipes) | NO LEAK | 0.0% | 0.072 | Both nodes |
| Apr 29 Leak (different pipes) | LEAK | 0.0% | 0.077 (n01) / 0.038 (n02) | No model response; node02 sensor failure (see 2.6) |
| Apr 30 AM No-Leak | NO LEAK | 0.0% | 0.07 (n01) / 0.01 (n02) | Both nodes silent |
| Apr 30 AM Leak | LEAK | 0.0% | 0.13 (n01) / 0.06 (n02) | Confidence rises but no leak3 events; small but significant uptick (p < 0.000001) |
| **Apr 30 PM No-Leak** | NO LEAK | 46.9% (n01) / 46.8% (n02) | 0.448 / 0.383 | **False-lock event: model fires for ~50 min in middle of no-leak session** |

**Interpretation — model behavior is more inconsistent than initial readings suggested:**
Across nine documented sessions, the model produced the desired three-phase pattern (low baseline → rise during leak → drop in recovery) on exactly one session (April 28 PM). On every other session the model is either silent in both conditions, fires constantly during no-leak, or — as observed on April 30 PM — spuriously locks on for 30+ minutes in the middle of a no-leak session.

The April 30 PM false-lock event is the clearest counter-evidence to the "model adapts to environment" hypothesis advanced after April 28: in this session both nodes (on different pipes) simultaneously transitioned from `confidence_score = 0` to `confidence_score > 0.9` at minute 5 of a no-leak session, held the high state for ~50 minutes, then transitioned back to `confidence_score = 0` for the remainder. There was no environmental change or sensor manipulation that explains this — it appears to be a recurring failure mode of the model itself.

**Honest read:** The April 28 PM result is real but not reproducible. The model cannot be claimed as a validated leak detector across sessions. Within-session signal exists in some sessions (April 27, April 28 PM, April 30 AM); does not exist in others (April 29, April 30 PM); and the model produces extended false-positive events that cannot be explained by ground truth or sensor behavior.

**Caveats:** Cross-session reproducibility on a fixed configuration has not been demonstrated. A locked, version-controlled model evaluated against held-out test data is required before any production claim. The handheld use case (device sees a new pipe every inspection) cannot be supported by the current model.

### 2.4 Architectural Implication
The composite alarm architecture (single-sensor breach AND ML confidence) is sound, but neither component is currently a validated leak detector on this rig:
- **Raw sensor channels** show statistically significant shifts during some leak windows (Apr 30 AM most clearly), but the direction and pattern of those shifts cannot be unambiguously distinguished from room-drift behavior observed in equivalent no-leak windows. They function as anomaly bounds — useful for catching events like operator handling, sensor disconnection, or extreme environmental change, but not as standalone leak detectors.
- **The ML model** produces inconsistent behavior across sessions: the desired three-phase pattern on April 28 PM, no response at all on April 29 and April 30 AM, and an unexplained false-lock event on April 30 PM. It is not currently a reliable detector.

The architecture itself is sound. The cloud layer correctly ingests, stores, evaluates, and routes alerts based on the data it receives — that pipeline has been validated end-to-end across 49,885 payloads spanning 6 days. The remaining gaps are at the **data and model** layer: the leak stimulus methodology does not exercise the sensors meaningfully (Section 1.3), and the ML model is not stable enough across sessions for production use. In a deployment with realistic stimulus and a locked, validated model, the composite-alarm cross-validation design would still be the correct approach.

### 2.5 Multi-Node Validation (April 30)
On April 30, both `node01` and `node02` were online simultaneously for the first time, deployed on different pipes in the same room. Dr. Caglayan had recommended placing both nodes on the same pipe to validate inter-node consistency; due to time constraints this exact test was not run, but the simultaneous deployment on different pipes provided equivalent evidence on the environmental channels.

**Side-by-side comparison during simultaneous sessions (different pipes, same room):**

| Channel | Apr 30 AM No-Leak | Apr 30 AM Leak |
|---|---|---|
| Moisture mean — node01 / node02 | 50.61 / 50.04 (Δ 0.58) | 44.87 / 45.24 (Δ 0.37) |
| Temperature mean — node01 / node02 | 24.23 / 24.31 (Δ 0.07) | 26.25 / 26.14 (Δ 0.12) |
| Acoustic mean — node01 / node02 | 26,515 / 26,013 (Δ 502) | 26,705 / 26,120 (Δ 584) |
| Vibration mean — node01 / node02 | 257 / 178 (Δ 79) | 282 / 188 (Δ 94) |

**Findings:**
- **Moisture and temperature agree across nodes within ~0.6%** during both no-leak and leak windows. Independent sensor hardware on different pipes produces nearly identical environmental readings, evidence that the firmware, sensor selection, and calibration are consistent across deployment instances.
- **Acoustic and vibration differ between nodes** by ~500 raw and ~80 raw respectively. This is expected — these channels measure pipe-local mechanical signal, and the two pipes are physically different. The fact that the *deltas* between no-leak and leak windows are similar across nodes (acoustic Δ 190 vs 107; vibration Δ 25 vs 9) suggests both nodes respond similarly to the same stimulus.
- **Both nodes detected the same direction and approximate magnitude of shift during the leak window** for moisture (both ↓~5%) and temperature (both ↑~2°C), with statistical significance p < 0.000001 on each channel. Cross-node agreement on shift direction is meaningful corroborating evidence — it is unlikely that two independent sensors on different pipes would coincidentally show the same drift pattern.
- However, as noted in Section 1.3, the *direction* of those shifts (moisture down, temp up) matches the room-drift pattern observed in long no-leak sessions, so attribution to the leak specifically remains uncertain.

**Implication:** Multi-node deployment works as designed. Both nodes produce equivalent baselines and respond consistently to the same stimulus. The cloud layer's per-node CloudWatch metric routing (using `${device_id}` substitution in the IoT Rule) correctly handles multiple nodes without code duplication.

### 2.6 Known Data Quality Issues
- **April 29 `node02` moisture/temperature anomaly.** During the April 29 leak window (18:50–19:20), `node02` moisture readings averaged 91.2% with a maximum of 100%, and temperature readings averaged 32.6°C with a maximum of 34°C. These values are inconsistent with `node01` readings during the same window (moisture ~48%, temperature ~26.5°C) and inconsistent with environmental conditions in the room. Most likely explanations are (a) water from the leak directly contacted the `node02` BME680 sensor, (b) a wire connection became loose, or (c) a sensor failure. `node02` data from this session was excluded from analysis. The cause was not investigated before the test rig was disassembled.
- **April 23 `node01` data.** The April 23 leak test was run before timestamps for the leak start/stop were logged, so the data exists but the leak boundaries cannot be reliably identified. Used only for general baseline reference.

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
- **Same-pipe multi-node validation.** Section 2.5 demonstrated that both nodes produce consistent readings when deployed on different pipes in the same room. Dr. Caglayan's recommended same-pipe test (both nodes clamped to the identical pipe) would isolate inter-node sensor variation from inter-pipe variation. This was not run before stack teardown due to time constraints.
- **Model stability and validation.** Lock a single trained model version, evaluate its performance against held-out per-session test data, and version-control the deployed model. The April 30 PM false-lock event (Section 2.3) is a known unexplained failure mode that needs root-cause analysis before any production claim.
- **Publish `leak_level` as a CloudWatch metric** once the model is stable enough to make it useful.
- **Investigate April 29 `node02` sensor failure.** Moisture pinned at 100% and temperature jumping to 34°C during a single session is not normal sensor behavior. Either the BME680 was directly water-exposed, a wire connection became loose, or the sensor failed. Determining the cause would inform handheld device weatherproofing design.

---

## 8. Advisor Q&A Prep — Likely Questions

**Q: Why don't your moisture thresholds cleanly separate leak from no-leak?**
The test rig's leak simulation method (a small bleed valve into a contained bucket) does not unambiguously produce the conditions our raw sensors are positioned to detect — water on the pipe exterior, flow disruption, or surface temperature change. The April 30 morning test did show statistically significant moisture and temperature shifts during the leak window on both nodes (p < 0.000001 on each channel, both nodes), but the *direction* of those shifts matches the slow room-drift pattern we observe in long no-leak sessions, so we cannot attribute them definitively to the leak stimulus rather than to time elapsed during the test. Our thresholds are set as anomaly-detection bounds rather than leak-validated bounds.

**Q: Is the ML model detecting leaks?**
Within some sessions, yes. The April 28 PM session showed the discriminating behavior expected of a working classifier — low pre-leak baseline, statistically significant rise during leak (p < 0.0001), and a sharp drop in recovery. The April 27 session showed a similar three-phase response. However, across nine analyzed sessions the model produced this desired pattern in only one. In other sessions the model is silent in both no-leak and leak conditions; in at least one case (April 30 PM) it spuriously locked into high-confidence "leak" output for ~50 minutes during a confirmed no-leak session, on both nodes simultaneously, with no environmental change to explain it. The model is not currently a reliable detector across sessions. Within-session signal exists in some configurations and not others, and the model produces unexplained false-positive events. A locked, version-controlled model evaluated against held-out test data is required before any production claim.

**Q: Do both nodes work? Did you validate multi-node operation?**
Yes — April 30 was the first day both nodes ran simultaneously, deployed on different pipes in the same room. Their environmental readings agreed within 0.6% on moisture and 0.1°C on temperature during both no-leak and leak windows, indicating the sensor selection, firmware, and calibration are consistent across hardware instances. Both nodes also showed the same direction and approximate magnitude of shift during the leak window on raw sensor channels. Dr. Caglayan recommended a same-pipe test to isolate inter-node sensor variation from inter-pipe variation; that test wasn't run before stack teardown but is documented as future work.

**Q: Why is your composite alarm structured the way it is?**
The composite alarm requires a single-sensor threshold breach AND a confidence breach to fire SNS. This cross-validation design reduces false positives that either signal would produce alone — and that's exactly what happened on April 30 PM, where the confidence channel firing alone for 50 minutes did *not* trigger SNS because no threshold alarm fired alongside it. The composite design correctly suppressed a false alert. On this rig neither component is currently reliable enough to fire on its own, but the architecture itself is doing what it was designed to do.

**Q: What would you do differently with more time?**
Four things in priority order: (1) lock and version-control a single trained ML model and root-cause the April 30 PM false-lock event; (2) develop a leak stimulus method that actually exercises sensor detection conditions; (3) move from absolute thresholds to rate-of-change alarms to handle environmental drift; (4) deploy in a realistic environment without a co-located circulation motor.

**Q: How did you analyze the data?**
CloudWatch dashboards show 1-minute averaged data, which smooths out the model's per-second behavior and hides extended events from view. To analyze the actual model output we exported the full DynamoDB record (49,885 rows across 6 days, sampled every ~2 seconds), and used Python (pandas, scipy.stats) to do phase-segmented statistical comparisons, rolling window analysis, and Mann-Whitney U tests on leak vs no-leak distributions across all sessions and both nodes. The per-second analysis is what surfaced both the within-session ML signal that the dashboards were hiding *and* the false-lock failure mode that wasn't visible at minute-level aggregation.

---

## 9. Personal Contribution Log (for Grading)

- CDK stack (IoT Core, DynamoDB, CloudWatch, SNS, IAM, backups, dashboard)
- mTLS device authentication with X.509 certificates
- IoT Rules Engine routing + per-node CloudWatch metrics
- Composite alarm cross-validation design
- Baseline characterization and threshold tuning (April 17–30 analysis sessions)
- Identification of leak stimulus methodology limitation (Section 1.3)
- Per-second statistical analysis across 49,885 payloads / 6 days / 9 sessions, revealing within-session ML signal, the April 30 PM false-lock failure mode, and across-session model instability (Section 2.3)
- Multi-node validation analysis demonstrating cross-node consistency on Apr 30 (Section 2.5)
- CloudWatch dashboard per-node layout
- Composite alarm demonstration via `set-alarm-state` for final report screenshots
- README, wiki structure, project board setup
- Milestone and issue organization (5 milestones, 10+ user stories, 30+ issues)
- This documentation
- [add as you go]
