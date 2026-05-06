# Enki — Hybrid Multi-Modal Leak Detection System
**ENGR 4380 - Senior Design 2 / CSEC 4390 – Practicum | Spring 2026**  
**Faculty Advisors:** Dr. Okan Caglayan & Dr. Gonzalo Parra  
**Course:** Engineering & Cybersecurity Systems

> A leak detection alert system using cross-integration of microcontrollers for data collection, cloud computing for alerts and monitoring, and machine learning running on every node — both fixed sensor units and a standalone handheld inspection device.

---

## 👥 Team

| Name | Role | GitHub |
|---|---|---|
| Moses Chavez | Cloud Infrastructure & DevOps | [@mwchavez](https://github.com/mwchavez) |
| Andres Varela | Hardware & Sensor Integration | [@Avarela314](https://github.com/Avarela314) |
| Ethan Garcia | ML Model Development & Training | [@shamumonky](https://github.com/shamumonky) |
| Carolina Flores | Team Leader & Hardware Design | [@CarolinaFUIW26](https://github.com/CarolinaFUIW26) |

---

## 🔗 Quick Links

- 📖 **[Full Documentation (Wiki)](../../wiki)** — Architecture decisions, debugging guides, and final report
- 📋 **[Project Board](../../projects)** — Milestone tracking and Story Point ledger
- 🎬 **Demo Video** — *(link pending)*

---

## 🏗️ System Overview

Enki is a leak detection system that combines **distributed continuous monitoring** with **on-demand handheld inspection**. Every node — fixed or portable — runs a TensorFlow Lite leak classification model directly on its ESP32, and the cloud layer cross-validates the model's confidence with rule-based threshold alarms.

**Distributed Monitoring (Fixed Nodes)**  
Sensor nodes clamped to pipes run on-device inference and publish four sensor readings plus the model's confidence score to AWS at ~1 Hz. The cloud pipeline ingests, stores, and evaluates the data through a composite alarm that fires only when both a threshold breach and the ML model agree — reducing false positives over either signal alone.

**Handheld Inspection (Standalone)**  
A portable ESP32 device shares the exact same firmware logic as the fixed nodes, minus WiFi and AWS connectivity. A technician holds the device against a pipe, the model runs locally, and the LCD displays "Leak" or "No Leak." No cloud connection required — useful for inspecting pipes that aren't covered by fixed sensors.

---

## 🔀 Architecture

```
┌────────────────────────────────────────────────────────────────┐  ┌─────────────────────────────────────┐
│           DISTRIBUTED MONITORING (Fixed Nodes)                 │  │   HANDHELD INSPECTION (Standalone)  │
│                                                                │  │                                     │
│   Fixed Sensor Nodes (ESP32-S3)                                │  │   Handheld Device (ESP32-S3)        │
│   [BME680] [ADXL335] [INMP441]                                 │  │   [BME680] [ADXL335] [INMP441]      │
│            │                                                   │  │            │                        │
│            │  On-device TFLite inference                       │  │            │  On-device TFLite      │
│            │  → 4 sensor values + confidence_score             │  │            ▼                        │
│            │                                                   │  │      LCD Display:                   │
│            │  MQTT over TLS (port 8883)                        │  │      "Leak" / "No Leak"             │
│            ▼                                                   │  │                                     │
│      AWS IoT Core (MQTT broker + Rules Engine)                 │  │   No WiFi, no cloud — fully offline │
│            │                                                   │  │                                     │
│            ├──────────────────────┐                            │  └─────────────────────────────────────┘
│            ▼                      ▼                            │
│       DynamoDB              CloudWatch Metrics                 │
│   (Historical record)       (per-node, 5 metrics)              │
│                                   │                            │
│                                   │  Per-node alarms           │
│                                   ▼                            │
│            ┌─────────────────────────────────────┐             │
│            │       Composite Alarm               │             │
│            │  (any threshold) AND (confidence)   │             │
│            └─────────────────────────────────────┘             │
│                                   │                            │
│                                   ▼                            │
│                          SNS → Email Alert                     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

The two systems share identical firmware and ML inference logic but differ in their output path: fixed nodes push to the cloud for fleet-wide monitoring, the handheld renders results locally for spot-checks.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- AWS CLI configured with credentials for the deployment account
- AWS CDK v2 (`npm install -g aws-cdk`)
- Provisioned X.509 certificates per device (uploaded to AWS Secrets Manager — see `cloud_infrastructure/docs/`)

### Deploy the Cloud Stack

```bash
# Clone the repo
git clone https://github.com/mwchavez/enki-leak-detection.git
cd enki-leak-detection/cloud_infrastructure/aws_backend_CDK

# Install Python dependencies
pip install -r requirements.txt

# One-time bootstrap (per account/region)
cdk bootstrap aws://<ACCOUNT_ID>/us-east-2

# Deploy with required parameters
cdk deploy \
  --parameters CertArnNode-01=<node-01 cert ARN> \
  --parameters CertArnNode-02=<node-02 cert ARN> \
  --parameters AlertEmail=<your-email@example.com>
```

After deploy, confirm the email subscription that SNS sends, then verify the dashboard at CloudWatch → Dashboards → `Leak_Detection_Dashboard`.

---

## ☁️ AWS Cloud Services

| AWS Service | Role | Why It's Used |
|---|---|---|
| **IoT Core** | MQTT broker & device gateway | Managed service; handles device authentication with X.509 certificates — no custom broker needed |
| **DynamoDB** | Raw sensor data storage | NoSQL with on-demand scaling; handles high-frequency sensor writes with single-digit millisecond latency |
| **CloudWatch** | Threshold alerting, dashboards & composite alarms | Native AWS monitoring; metric alarms + composite alarm logic eliminate the need for custom processing code |
| **SNS** | Alert notifications | Delivers email alerts when the composite alarm fires |
| **IAM** | Access control | Least-privilege roles scoped per service; IoT Rules Engine assumes a role to write to DynamoDB |
| **Secrets Manager** | Device certificate storage | Private keys and certs stored as secrets and retrieved by deploy scripts — never committed to git |
| **AWS Backup** | DynamoDB backup vault | Daily automated backups of sensor history with 7-day retention; protects against accidental table changes |
| **AWS CDK** | Infrastructure as Code | Entire cloud stack defined in Python; parameterized and portable across AWS accounts |

---

## 🔧 Edge & ML Stack

| Component | Role | Details |
|---|---|---|
| **ESP32-S3** | Microcontroller | Drives both fixed nodes and the handheld device; identical firmware on each |
| **BME680** | Environmental sensor | Provides temperature and humidity (moisture) readings near the pipe |
| **ADXL335** | Accelerometer | Detects pipe vibration anomalies |
| **INMP441** | I2S digital microphone | Acoustic sensing for pipe resonance detection |
| **TensorFlow Lite** | Edge ML framework | Runs leak classification model directly on the ESP32; outputs a 0.0–1.0 confidence score |
| **LCD Display** | Handheld output | Renders "Leak" / "No Leak" verdict on the standalone handheld device |

---

## 📡 Sensor Data Schema

Each fixed node publishes JSON payloads via MQTT to the topic pattern `leaksensor/<node-id>/data`:

```json
{
  "device_id": "node-01",
  "timestamp": 1745601234,
  "moisture": 50.4,
  "temperature": 24.3,
  "vibration": 714,
  "acoustic": 28482,
  "confidence_score": 0.23
}
```

> **Note:** Acoustic and vibration values are currently published as **raw sensor units** rather than calibrated Hz / g-force. Schema-to-firmware unit calibration is tracked as future work (see Section below). The example values above are representative of post-clamp baseline readings collected on April 22–23, 2026.

| Field | Type | Description |
|---|---|---|
| `device_id` | String | Unique identifier for the sensor node (DynamoDB partition key) |
| `timestamp` | Number | Unix epoch in seconds (DynamoDB sort key) |
| `moisture` | Number | Relative humidity / moisture percentage near the node |
| `temperature` | Number | Ambient temperature in Celsius |
| `vibration` | Number | Vibration intensity (raw ADXL335 reading) |
| `acoustic` | Number | Acoustic intensity (raw INMP441 reading) |
| `confidence_score` | Number | On-device ML model's leak confidence (0.0 – 1.0) |

---

## 🚨 Alert Logic

Each per-node metric is evaluated against an anomaly-detection threshold; the composite alarm fires only when a threshold breach co-occurs with a high model confidence score. This cross-validation is the actual leak-detection mechanism.

| Channel | Threshold | Notes |
|---|---|---|
| Moisture | `> 55%` | Above observed post-clamp baseline maximum (~53.6%) |
| Temperature | `> 26°C` | Headroom over baseline maximum (~24.5°C) for normal room thermal drift |
| Acoustic | `> 29,500` (raw) | Above baseline maximum (~29,006) on the test rig |
| Vibration | `> 900` (raw) | Above baseline maximum (~831) on the test rig |
| Confidence Score | `≥ 0.8` | ML model's leak verdict |
| **Composite Alarm** | `(any threshold breach) AND (confidence ≥ 0.8)` | Triggers SNS email |

All alarms require **3 consecutive evaluation periods** (~3 minutes) before firing, filtering out single-period transients.

> **Design Decision:** Thresholds and ML confidence are kept as independent signals and combined only at the composite alarm. Thresholds give debuggable, deterministic anomaly bounds; the ML model captures multi-modal correlations no single threshold can express. Requiring agreement between the two reduces false positives over either signal alone. Threshold values are currently set as **anomaly-detection bounds** above the observed baseline rather than as validated leak-separation bounds — see the Future Work section for the test-rig limitation that drove this choice.

---

## 📁 Repository Structure

```
enki-leak-detection/
├── cloud_infrastructure/        # AWS CDK stack (Python)
│   ├── aws_backend_CDK/
│   └── docs/
│        ├── Architecture.md
│        └── gathering_data.md
├── ml_training/                 # ML model training & dataset generation
│   ├── train_fusion_model.py
│   ├── generate_fake_dataset.py
│   ├── leak_fusion_model.tflite
│   ├── norm_mu.csv
│   └── norm_sigma.csv
├── pipe_nodes/                  # ESP32 firmware for fixed sensor nodes
├── end_user_concept/            # Homeowner-facing dashboard concept (Google AI Studio)
├── handheld_device/             # (Planned) ESP32 firmware for handheld
├── wiki/
│   └── Debugging-and-Logs.md
└── README.md
```

---

## ✅ Progress

### Cloud Infrastructure (Moses)
- [x] AWS account setup with IAM least-privilege
- [x] AWS IoT Core provisioned with X.509 device certificates
- [x] DynamoDB table configured (partition key: `device_id`, sort key: `timestamp`)
- [x] IoT Rules Engine routing MQTT → DynamoDB
- [x] IAM Role for IoT → DynamoDB write permissions
- [x] End-to-end MQTT → IoT Core → DynamoDB pipeline tested
- [x] SNS Topic with email subscription
- [x] Infrastructure defined as code with AWS CDK (Python)
- [x] Per-node CloudWatch metrics via `${device_id}` substitution
- [x] CloudWatch threshold alarms (moisture, temperature, acoustic, vibration, confidence)
- [x] Composite alarms for ML confidence × threshold cross-validation
- [x] CloudWatch dashboard with per-node graphs and System Status widget
- [x] AWS Backup vault with daily DynamoDB snapshots (7-day retention)
- [x] Device certificates migrated to AWS Secrets Manager
- [x] Baseline characterization & threshold tuning (April 22–23 testing)
- [x] End-user dashboard concept (homeowner-facing UI prototype)
- [ ] Refinement

### Hardware & Sensors (Andres, Carolina)
- [x] Sensor data sheets compiled
- [x] Bill of materials finalized
- [x] ESP32 WiFi connection and MQTT data transfer tested
- [x] Fixed pipe node prototype assembly
- [x] Pipe-clamp ("clam") fixtures fabricated and deployed
- [x] Handheld device CAD design
- [x] Handheld device assembly
- [ ] Refinement

### ML Model (Ethan)
- [x] Fake dataset generator for training
- [x] TFLite model trained and exported
- [x] Normalization parameters saved (norm_mu.csv, norm_sigma.csv)
- [x] Embedded AI deployment on ESP32-S3
- [x] Handheld integration and field testing
- [x] Multi-session test data collection (no-leak baselines + leak simulation)
- [ ] Refinement

---

## 🔐 Security Practices

- **No root account usage** — IAM user with scoped permissions only
- **Certificate-based mutual TLS** — X.509 certificates authenticate every IoT device
- **Least-privilege IoT policies** — device policies scoped to specific MQTT topics (`leaksensor/<node-id>/data`)
- **IAM Roles over IAM Users** — services assume temporary roles; the IoT Rules Engine has only `dynamodb:PutItem` permission on the sensor table
- **Secrets Manager for device credentials** — private keys, device certs, and the Amazon Root CA are stored as managed secrets rather than in repo files; deploy scripts retrieve them at provisioning time
- **CDK parameterization** — certificate ARNs and the alert email are passed as `CfnParameter` at deploy time, never hardcoded
- **Secrets excluded from version control** — `.gitignore` excludes any local cert artifacts, WiFi credentials, and `cdk.out`

---

## 🔭 Future Work

- **Leak stimulus methodology.** The current test rig uses a small bleed valve into a contained bucket, which doesn't produce conditions sensors are positioned to detect (water on the pipe exterior, flow disruption, surface temperature change). Future testing should exercise these conditions directly.
- **Baseline subtraction for motor noise.** The closed-loop test rig is dominated by its circulation motor on the acoustic and vibration channels. Characterizing and subtracting the motor signature would improve signal-to-noise for those modalities.
- **Variance and rate-of-change alarms.** Some leak signatures show up as variance shifts even when the mean stays flat. CloudWatch Metric Math (`RATE()`, `STDDEV()`) and Anomaly Detection alarms could capture this without additional firmware work.
- **Deployment in a realistic environment.** Building plumbing with longer pipe runs and no co-located circulation motor would let the acoustic and vibration channels function as designed.
- **Sensor calibration pass.** Convert raw acoustic and vibration values to calibrated Hz / g-force units to match the documented schema.
- **Multi-node validation.** Confirm both nodes produce consistent baselines and respond similarly to stimuli once node-02 is fully online.

---

## 📊 Individual Contribution Summary

> Per the Capstone Project Guide, contribution is measured in completed Story Points from the Project Board.

| Team Member | Total Story Points Completed | Contribution % |
|---|---|---|
| Moses Chavez | 35 | **37.6%** |
| Andres Varela | 23 | **24.7%** |
| Ethan Garcia | 24 | **25.8%** |
| Carolina Flores | 11 | **11.8%** |
| **Team Total** | 93 | **100.0%** |

---

*Spring 2026 — University of the Incarnate Word | ENGR 4380 - Senior Design 2 / CSEC 4390 – Practicum*
