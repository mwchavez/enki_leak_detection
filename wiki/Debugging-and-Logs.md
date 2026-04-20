# Debugging & Reading Logs

> **Audience:** Enki team members + anyone operating the cloud pipeline during demos.
> **When to use:** A sensor node stops publishing, an alarm fires (or doesn't fire when it should), emails aren't arriving, or DynamoDB looks empty. Start here before opening a dozen AWS console tabs.

---

## 1. Data Flow Refresher

When something breaks, it's almost always at one of these boundaries. Knowing the flow tells you where to look first:

```
ESP32 Node  ──(MQTT/TLS)──►  IoT Core  ──(Topic Rule)──►  ┬──► DynamoDB
                                                          └──► CloudWatch Metrics ──► Alarms ──► SNS ──► Email
```

Work the pipeline **left to right**. If DynamoDB is empty, don't start by debugging DynamoDB — check whether IoT Core is even receiving the MQTT publish.

---

## 2. Quick Triage Table

| Symptom | Most Likely Cause | First Place to Look |
|---|---|---|
| Device won't connect at all | Cert not attached to Thing, or policy missing `iot:Connect` | IoT Core → Monitor → Logs (filter by `ClientId`) |
| Device connects, disconnects immediately | Policy missing `iot:Publish` or `iot:Subscribe` for the topic | Same as above, look for `AUTHORIZATION_FAILURE` |
| Messages publishing but DynamoDB empty | Topic Rule SQL not matching, or IoT → DynamoDB IAM role broken | IoT Core → Act → Rules → `LeakDetectionTopicRule` → Rule metrics |
| DynamoDB has rows, but CloudWatch metrics are flat | Metric action in Topic Rule failing (usually field name mismatch in the `${...}` substitution) | CloudWatch → Metrics → `Enki/LeakDetection` namespace |
| Metrics look right but alarm never fires | Threshold wrong, or `evaluation_periods` hasn't been reached yet | CloudWatch → Alarms → view the graph with threshold overlay |
| Alarm is in ALARM state but no email | SNS subscription never confirmed (check inbox for the confirmation email) | SNS → Topics → `LeakAlertTopic` → Subscriptions |

---

## 3. Debugging by Component

### 3.1 IoT Core — Is the device connecting and publishing?

**CloudWatch log group:** `AWSIotLogsV2`
IoT Core logging must be enabled (V2 logging, set to at least `INFO` for debugging; drop back to `WARN` or `ERROR` when things are stable to control costs).

**What to filter for:**
- `"EventType": "Connect.AuthError"` → cert or policy issue
- `"EventType": "Publish.AuthError"` → policy doesn't allow publish on the topic they're trying to use
- `"EventType": "RuleExecution"` → confirms the Topic Rule actually fired

**Useful CLI sanity check — is the Thing alive?**
```bash
aws iot list-things
aws iot list-thing-principals --thing-name <node_name>
```
If `list-thing-principals` returns empty, your cert isn't attached — check the `CfnThingPrincipalAttachment` in the stack.

> **TODO:** Add the specific `AUTHORIZATION_FAILURE` message you hit during initial provisioning + how you fixed it. That was a real debugging session and other team members will hit it too.

---

### 3.2 IoT Topic Rule — Are messages being routed?

The rule in `leak_detection_practicum_stack.py` has the SQL `SELECT * FROM 'leaksensor/+/data'`. Every field referenced in downstream actions (`${device_id}`, `${moisture}`, etc.) has to exist in the published JSON payload **with the exact same key name** — a typo like `Moisture` vs `moisture` will silently drop that metric action.

**Where to look:**
- CloudWatch → Metrics → `AWS/IoT` namespace → `RuleMessageThrottled`, `Failure`, `Success` per rule name
- If you see `Success` going up but a specific metric action is failing, check `ActionExecution` failures filtered by `ActionType=CloudwatchMetric`

**Republish a test payload from the AWS console:**
IoT Core → Test → MQTT test client → Publish to `leaksensor/node-01/data` with the schema from the README. If that lands in DynamoDB but the real device's payloads don't, the payload JSON from the firmware is malformed.

---

### 3.3 DynamoDB — Are writes actually landing?

```bash
aws dynamodb scan \
  --table-name <table-name-from-cfn-output> \
  --limit 5
```

If this returns items but your node's `device_id` isn't among them, the Topic Rule is working for other nodes — it's something specific to that one device's payload.

On-demand billing means there's no throttling to blame. If writes aren't showing up, it's almost always the IAM role (`IoTCoreDynamoWriteRole`) or the SQL statement, not DynamoDB itself.

---

### 3.4 CloudWatch Metrics — Is the data visible for alarming?

Metrics live in the `Enki/LeakDetection` namespace with names like `node-01_moisture`.

```bash
aws cloudwatch list-metrics --namespace "Enki/LeakDetection"
```

**Common gotcha:** CloudWatch metrics have a resolution floor — if you publish faster than once per second, you're paying for high-resolution metrics whether you meant to or not. The current alarms use default (60-second) resolution, so publishing every few seconds is fine.

---

### 3.5 CloudWatch Alarms — Why didn't the alarm fire?

Every alarm in the stack uses `evaluation_periods = 3`, meaning the threshold has to be breached for **3 consecutive periods** before going to ALARM. If you're testing with a short burst of bad data, the alarm may never leave OK state. For demo purposes, either:
- Sustain the bad input longer, or
- Temporarily drop `evaluation_periods` to 1 during testing (remember to put it back).

**Check an alarm's state from CLI:**
```bash
aws cloudwatch describe-alarms --alarm-names "Alarm for High Moisture node-01"
```

The composite alarm (`LeakDetectionCompositeAlarm_<node>`) requires **both** a threshold alarm AND the confidence score alarm to be in ALARM. If the ML confidence metric isn't being published (handheld device or firmware not sending it), the composite alarm will never fire even if moisture is through the roof.

---

### 3.6 SNS — Are emails being delivered?

The #1 cause of "my alarm fired but I didn't get an email" is an **unconfirmed subscription**. When you first deploy, AWS sends a confirmation email with a link that has to be clicked. Until it's clicked, the subscription is in `PendingConfirmation`.

```bash
aws sns list-subscriptions-by-topic --topic-arn <LeakAlertTopic ARN>
```

Look at the `SubscriptionArn` field. If it literally says `PendingConfirmation`, go find the confirmation email (check spam).

**Force a test alarm:**
```bash
aws cloudwatch set-alarm-state \
  --alarm-name "Alarm for High Moisture node-01" \
  --state-value ALARM \
  --state-reason "Manual test"
```
You should get an email within a minute or two. This is the fastest way to prove the SNS wiring works without needing to manipulate real sensor data.

---

## 4. Log Groups Reference

| Log Group | What's in it | When to check |
|---|---|---|
| `AWSIotLogsV2` | All IoT Core events (connect, publish, rule execution, auth failures) | Any device-side issue |
| `/aws/events/...` | EventBridge (only relevant if Backup events fire) | Backup plan debugging |
| `AWS/IoT` metric namespace (not a log group, but adjacent) | Rule success/failure counts | Topic Rule not routing |

> **TODO:** If we add a Lambda downstream later (e.g., for pre-processing ML features before DynamoDB), its log group (`/aws/lambda/<function-name>`) goes here.

---

## 5. Known Gotchas We've Hit

*This section is the most valuable part of this page over time — it's where lessons learned live. Add to it every time the team loses more than 30 minutes to something.*

- **[ADD] Cert ARN parameter mismatch between `cdk deploy` and the attachment resource** — describe what the error looked like.
- **[ADD] MQTT topic name mismatch between firmware and policy** — node name casing, etc.
- **[ADD] Any CDK synth errors you hit and the fix.**

---

## 6. Fast Commands Cheat Sheet

```bash
# Is my Thing registered and cert-attached?
aws iot list-thing-principals --thing-name node-01

# Any messages hitting the topic rule recently?
aws cloudwatch get-metric-statistics \
  --namespace AWS/IoT \
  --metric-name Success \
  --dimensions Name=RuleName,Value=LeakDetectionTopicRule \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 300 \
  --statistics Sum

# Latest 5 rows for a node
aws dynamodb query \
  --table-name <table-name> \
  --key-condition-expression "device_id = :d" \
  --expression-attribute-values '{":d":{"S":"node-01"}}' \
  --limit 5 \
  --scan-index-forward false

# Force-trigger an alarm end-to-end (proves SNS works)
aws cloudwatch set-alarm-state \
  --alarm-name "Alarm for High Moisture node-01" \
  --state-value ALARM \
  --state-reason "Manual test"
```

---

*Last updated: [DATE] by [NAME]. If you debugged something new, add it to Section 5 before you forget.*
