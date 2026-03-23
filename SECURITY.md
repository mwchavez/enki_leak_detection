# Security Policy — Enki Leak Detection System

This document describes the security practices, controls, and design decisions for the Enki hybrid leak detection system. It is intended as a reference for team members, faculty advisors, and anyone reviewing the project's security posture.

---

## Threat Model Overview

Enki operates across two attack surfaces: a cloud pipeline (AWS IoT Core → DynamoDB → CloudWatch → SNS) and edge devices (ESP32-S3 microcontrollers on physical pipes). The security controls below are mapped to the threats they mitigate.

| Threat | Impact | Control |
|---|---|---|
| Rogue device publishes fake sensor data | False alerts or suppressed real leaks | Mutual TLS with per-device X.509 certificates |
| Compromised node impersonates another node | Polluted data for the wrong device_id | IoT policies scope each device to its own MQTT topic |
| Stolen credentials in source code | Unauthorized access to AWS resources | Secrets excluded from version control; CDK parameterization |
| Over-privileged service roles | Lateral movement if a role is compromised | Least-privilege IAM; roles scoped to single actions |
| Unauthorized changes to infrastructure code | Broken or insecure deployments | Branch protection with pull request reviews |
| Physical theft of an edge device | Attacker holds valid device certificate | Certificate revocation through AWS IoT Core |

---

## Device Identity & Authentication

Every ESP32 sensor node — whether a fixed pipe node or the handheld device — authenticates to AWS IoT Core using **mutual TLS with X.509 certificates**.

- Each device is provisioned with its own unique certificate. There are no shared credentials across nodes.
- Certificates are generated through the AWS Console and loaded onto the ESP32 using a Python provisioning script maintained by the team.
- IoT Core validates both the device's certificate and the broker's certificate during the TLS handshake (mutual authentication). A device without a valid, active certificate cannot connect.
- All MQTT communication occurs over **TLS on port 8883**. Plaintext MQTT (port 1883) is never used.

---

## Access Control

### AWS IAM — Least Privilege by Design

- **No root account usage.** All AWS operations are performed through IAM users with scoped permissions.
- **IAM Roles over IAM Users for services.** AWS services assume temporary roles rather than using long-lived credentials:
  - The IoT Rules Engine assumes a role with **only** `dynamodb:PutItem` on the sensor data table — it cannot read, scan, or delete data.
  - A separate role grants the IoT Rules Engine `cloudwatch:PutMetricData` for publishing sensor metrics. This role uses `Resource: "*"` because CloudWatch's PutMetricData API does not support resource-level permissions. This is a known AWS limitation, not an oversight.

### IoT Topic-Level Scoping

Each device's IoT policy restricts it to its own MQTT topic. For example, `node-01` can only:

- **Connect** as client ID `node-01`
- **Publish** to `leaksensor/node-01/data`
- **Subscribe** to `leaksensor/node-01/data`

This means that even if an attacker compromises one node's certificate, they cannot publish data as a different node or subscribe to other nodes' topics. The IoT Rules Engine's SQL query (`SELECT * FROM 'leaksensor/+/data'`) ingests from all nodes, but the devices themselves are isolated from each other.

### Repository Access Control

- The GitHub repository uses **branch protection rules** on the main branch.
- All changes require a **pull request with review** before merging. Direct pushes to main are not permitted.

---

## Data Protection

### In Transit

All data leaving an ESP32 travels over **TLS 1.2+ on port 8883** to AWS IoT Core. There is no unencrypted communication path between devices and the cloud.

### At Rest

DynamoDB encrypts all stored data at rest using **AWS-managed encryption keys** (the default configuration). This provides AES-256 encryption managed entirely by AWS with no additional configuration required.

---

## Secrets Management

- **Device certificates** (`.pem`, `.key` files), **WiFi credentials**, and **AWS resource ARNs** are excluded from version control.
- The `.gitignore` file is configured to prevent accidental commits of sensitive material.
- **CDK parameterization** is used for deployment-time secrets. Certificate ARNs are passed as `CfnParameter` values at deploy time rather than being hardcoded in the stack. This means the infrastructure code itself contains no secrets.

> **Action item:** Team members should periodically verify that the `.gitignore` covers all sensitive file patterns (e.g., `*.pem`, `*.key`, `certs/`, `config.h` with WiFi credentials).

---

## Incident Response — Device Compromise

If a physical device is stolen or a certificate is suspected to be compromised:

1. **Deactivate the certificate** in the AWS IoT Core console. This immediately prevents the device from connecting.
2. **Revoke the certificate** to permanently invalidate it.
3. **Review CloudWatch logs and DynamoDB records** for any anomalous data published by the compromised device ID during the exposure window.
4. **Provision a replacement certificate** for the new or recovered device using the team's Python provisioning script.

Because each device has its own certificate and its own topic-scoped policy, compromising one device does not affect the security of any other node in the system.

---

## Shared Responsibility Model

Enki runs on AWS, which means security is split between AWS and the team:

| Responsibility | Owner |
|---|---|
| Physical security of data centers, network infrastructure, and managed service internals | AWS |
| IoT Core MQTT broker availability and TLS termination | AWS |
| DynamoDB encryption at rest (AWS-managed keys) | AWS |
| Device certificate generation, distribution, and revocation | Enki Team |
| IAM policies, IoT policies, and least-privilege enforcement | Enki Team |
| Secrets management and `.gitignore` hygiene | Enki Team |
| Source code access control and branch protection | Enki Team |
| Physical security of edge devices in the field | Enki Team |

---

## Reporting a Security Issue

If you discover a security vulnerability in this project, please contact the team directly rather than opening a public issue. Reach out to any team member listed in the [README](README.md).

---

*Enki Leak Detection System — Spring 2026, University of the Incarnate Word*
