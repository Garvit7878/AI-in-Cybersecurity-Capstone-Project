<div align="center">

<img src="https://img.shields.io/badge/🛡️-AI_CYBERSECURITY_CAPSTONE-0B1929?style=for-the-badge&labelColor=0B1929" alt="header"/>

# AI-Based Threat Detection & Prevention System
#### *Enterprise Infrastructure Security — Autonomous Real-Time Defense Platform*

<br/>

[![Model](https://img.shields.io/badge/ML_Model-XGBoost_%7C_Deep_Autoencoder-00695C?style=flat-square&logo=scikitlearn&logoColor=white)](code/threat_detector_xai.py)&nbsp;&nbsp;[![XAI](https://img.shields.io/badge/XAI-SHAP_%2F_LIME-1565C0?style=flat-square&logo=openai&logoColor=white)](code/threat_detector_xai.py)&nbsp;&nbsp;[![Security](https://img.shields.io/badge/Defense-Adversarial_PGD-B71C1C?style=flat-square&logo=shield&logoColor=white)](generate_cybersecurity_pdf.py)&nbsp;&nbsp;[![Privacy](https://img.shields.io/badge/Privacy-Differential_Privacy_(GDPR)-6A1B9A?style=flat-square&logo=gnuprivacyguard&logoColor=white)](docs/deliverables/AI_Cybersecurity_Threat_Detection_Report.pdf)

<br/>

**Autonomous, real-time AI threat detection and prevention platform** for mid-sized enterprise infrastructure.  
Integrates streaming telemetry ingestion, hybrid ML/DL anomaly detection, adversarial defense,  
and plain-language Explainable AI (XAI) alert generation with automated SOAR response.

<br/>

---

<br/>

<table>
<tr>
<td align="center" width="160"><b>👤 Candidate</b></td>
<td align="center" width="160"><b>🎓 Roll Number</b></td>
<td align="center" width="220"><b>📧 Email</b></td>
<td align="center" width="160"><b>🔬 Domain</b></td>
</tr>
<tr>
<td align="center"><b>Garvit Sharma</b></td>
<td align="center">2301730190</td>
<td align="center"><a href="mailto:garvitsharma8909@gmail.com">garvitsharma8909@gmail.com</a></td>
<td align="center">AI in Cybersecurity</td>
</tr>
</table>

<br/>

📄 **Primary Deliverable:** [AI_Cybersecurity_Threat_Detection_Report.pdf](docs/deliverables/AI_Cybersecurity_Threat_Detection_Report.pdf)

<br/>

</div>

---

## Table of Contents

- [System Architecture](#-system-architecture)
- [Detection Pipeline Flow](#-detection-pipeline-flow)
- [Attack Identification & ML Strategy](#1-attack-type-identification--ml-detection-strategy)
- [Feature Engineering](#2-feature-engineering--justification)
- [Adversarial Defense](#3-adversarial-attack-vulnerability--mitigation)
- [Explainable AI Demo](#4-explainable-ai-xai-for-non-technical-stakeholders)
- [Ethics & Privacy](#5-ethical--privacy-governance)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)

---

## 🏗 System Architecture

> High-level overview of the five-tier autonomous defense platform.

```mermaid
graph LR
    subgraph INGEST["① Ingestion"]
        direction TB
        K["Apache Kafka<br/>50K events/sec"]
    end

    subgraph FEAT["② Feature Engineering"]
        direction TB
        FL["Apache Flink<br/>Sliding-Window Extractor"]
    end

    subgraph DETECT["③ Hybrid Detection"]
        direction TB
        XG["XGBoost<br/>Known Attacks"]
        AE["Deep Autoencoder<br/>Zero-Day Discovery"]
    end

    subgraph XAI["④ XAI Alerting"]
        direction TB
        SH["SHAP Engine<br/>Plain-English Narratives"]
    end

    subgraph SOAR["⑤ SOAR Response"]
        direction TB
        SR["Automated<br/>Containment"]
    end

    INGEST --> FEAT --> DETECT --> XAI --> SOAR

    style INGEST fill:#E0F2F1,stroke:#00695C,stroke-width:2px
    style FEAT fill:#E0F2F1,stroke:#00695C,stroke-width:2px
    style DETECT fill:#FFF3E0,stroke:#E65100,stroke-width:2px
    style XAI fill:#E8EAF6,stroke:#283593,stroke-width:2px
    style SOAR fill:#FCE4EC,stroke:#B71C1C,stroke-width:2px
```

### Data Sources Ingested

| Source | Protocol | Volume |
|:---|:---|:---|
| Network Traffic Flows | NetFlow / IPFIX | ~30K flows/sec |
| DNS & TLS Metadata | Zeek Sensor | ~10K queries/sec |
| Endpoint Telemetry | Windows Sysmon + EDR | ~8K events/sec |
| Cloud Audit Logs | AWS CloudTrail | ~2K events/sec |

---

## 🔄 Detection Pipeline Flow

> Detailed flow from raw telemetry to automated containment.

```mermaid
flowchart TD
    A["Raw Network Telemetry"] --> B["Apache Kafka Broker"]
    B --> C["Apache Flink: Sliding-Window Feature Extraction"]

    C --> D["Byte Transfer Velocity"]
    C --> E["DNS Shannon Entropy"]
    C --> F["Auth Failure Rate"]
    C --> G["Off-Hours Deviation"]
    C --> H["Connection Fanout"]

    D & E & F & G & H --> I{"Adversarial Defense Layer<br/>Feature Squeezing + Quantization"}

    I --> J["XGBoost / LightGBM<br/>Supervised Classification"]
    I --> K["Variational Autoencoder<br/>Unsupervised Anomaly Detection"]

    J --> L{"Threat<br/>Detected?"}
    K --> L

    L -- "Yes" --> M["SHAP / LIME Attribution Engine"]
    L -- "No" --> N["Log & Continue Monitoring"]

    M --> O["Executive Plain-Language Alert"]
    M --> P["SOAR Automated Response"]

    P --> Q["🔥 BGP Blackhole Malicious IP"]
    P --> R["🔒 Isolate Endpoint via EDR"]
    P --> S["🔑 Revoke Compromised Tokens"]

    style A fill:#E0F2F1,stroke:#00695C
    style I fill:#FFF3E0,stroke:#E65100
    style L fill:#FFF9C4,stroke:#F57F17
    style M fill:#E8EAF6,stroke:#283593
    style P fill:#FCE4EC,stroke:#B71C1C
    style Q fill:#FCE4EC,stroke:#B71C1C
    style R fill:#FCE4EC,stroke:#B71C1C
    style S fill:#FCE4EC,stroke:#B71C1C
```

---

## 🎯 Capstone Problem Statement & Solutions

### 1. Attack Type Identification & ML Detection Strategy

**Primary Attack Type:** Distributed Polymorphic Ransomware & Automated Multi-Stage Data Exfiltration

```
Lateral Movement  →  Internal Staging  →  Data Egress  →  Encryption Trigger
```

**Proposed AI/ML Strategy — Dual-Path Hybrid Inference:**

```mermaid
graph LR
    INPUT["Feature<br/>Vector"] --> PATH_A
    INPUT --> PATH_B

    subgraph PATH_A["Supervised Path"]
        A1["XGBoost Ensemble"] --> A2["Known Attack<br/>Classification"]
    end

    subgraph PATH_B["Unsupervised Path"]
        B1["Variational<br/>Autoencoder"] --> B2["Zero-Day<br/>Anomaly Score"]
    end

    A2 --> FUSE["Fusion Layer:<br/>Threat Decision"]
    B2 --> FUSE

    style PATH_A fill:#E0F2F1,stroke:#00695C,stroke-width:2px
    style PATH_B fill:#FFF3E0,stroke:#E65100,stroke-width:2px
    style FUSE fill:#FCE4EC,stroke:#B71C1C,stroke-width:2px
```

| Path | Model | Training Data | Strength |
|:---|:---|:---|:---|
| **Supervised** | XGBoost / LightGBM | CIC-IDS2017 + Enterprise Logs | Sub-millisecond detection of known signatures |
| **Unsupervised** | Variational Autoencoder (VAE) | Benign baseline flows only | Zero-day discovery via reconstruction loss threshold |

> Anomalies flagged when VAE reconstruction loss exceeds the dynamic 99.5th percentile threshold.

---

### 2. Feature Engineering & Justification

| Feature | Formulation | Why It Matters |
|:---|:---|:---|
| **Byte Transfer Velocity** | `Bytes / ΔTime` | Separates normal browsing from bulk exfiltration spikes |
| **DNS Shannon Entropy** | `-Σ pᵢ log₂(pᵢ)` | Catches algorithmically generated domains (DGA) and DNS tunneling |
| **Auth Failure Rate** | `Count in 60s window` | Exposes credential stuffing and brute-force password spraying |
| **Off-Hours Activity Score** | `\|t_access - μ_historical\|` | Identifies stolen credentials used outside business hours |
| **Connection Fanout** | `Distinct Dest IPs / 5 min` | Captures automated port scanning and worm lateral propagation |

```mermaid
graph LR
    RAW["Raw Telemetry"] --> FE["Feature Engineering<br/>(Apache Flink)"]
    FE --> V1["Byte Velocity"]
    FE --> V2["DNS Entropy"]
    FE --> V3["Auth Failures"]
    FE --> V4["Time Deviation"]
    FE --> V5["Conn. Fanout"]
    V1 & V2 & V3 & V4 & V5 --> ML["ML Detection<br/>Engine"]

    style RAW fill:#F5F5F5,stroke:#9E9E9E
    style FE fill:#E0F2F1,stroke:#00695C
    style ML fill:#FFF3E0,stroke:#E65100
```

---

### 3. Adversarial Attack Vulnerability & Mitigation

**Threat:** Evasion Attacks via Gradient Perturbation (FGSM / PGD)

> Adversaries inject non-functional packet padding and fragment flow durations to dilute byte velocity, pushing the feature vector across the decision boundary into the benign region.

**Defense Strategy:**

```mermaid
graph TD
    ATK["Adversarial Input<br/>(Perturbed Features)"] --> FS["Feature Squeezing<br/>Spatial Smoothing +<br/>Bit-Depth Quantization"]
    FS --> CLEAN["Cleaned Feature Vector"]
    CLEAN --> MODEL["Adversarially Hardened<br/>XGBoost Ensemble<br/>(PGD-Trained)"]
    MODEL --> DEC{"Accurate<br/>Classification"}

    style ATK fill:#FCE4EC,stroke:#B71C1C
    style FS fill:#FFF3E0,stroke:#E65100
    style CLEAN fill:#E0F2F1,stroke:#00695C
    style MODEL fill:#E8EAF6,stroke:#283593
    style DEC fill:#E8F5E9,stroke:#2E7D32
```

| Defense Layer | Technique | Effect |
|:---|:---|:---|
| **Pre-Inference** | Feature Squeezing & Quantization | Strips subtle noise perturbations from input vectors |
| **Training-Time** | PGD Adversarial Training | Model learns decision boundaries robust to gradient attacks |

---

### 4. Explainable AI (XAI) for Non-Technical Stakeholders

The platform embeds a **Semantic Translation Layer** that converts SHAP/LIME attribution values into actionable executive briefings:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  🛡️  AI SECURITY INCIDENT EXPLANATION (EXECUTIVE SUMMARY)             │
│─────────────────────────────────────────────────────────────────────────│
│  ALERT LEVEL: 🔴 HIGH RISK CRITICAL INCIDENT (Confidence: 99.8%)      │
│                                                                         │
│  WHAT HAPPENED?                                                         │
│  Anomalous outbound transmission detected from Workstation 10.0.14.88  │
│  to external server 198.51.100.24.                                     │
│                                                                         │
│  WHY DID THE AI TRIGGER THIS ALERT?                                    │
│  ├── 90.0%  Unusually Fast Data Transfer Speed (Exfiltration Spike)    │
│  ├──  5.3%  Repeated Failed Logins (7 brute-force attempts)            │
│  ├──  3.5%  Connection to Untrusted External Server                    │
│  └──  1.2%  Abnormally High Sensitive Data Volume                      │
│                                                                         │
│  AUTOMATED ACTIONS TAKEN:                                               │
│  ✅ Workstation 10.0.14.88 quarantined from local network              │
│  ✅ Outbound IP 198.51.100.24 blacklisted at perimeter firewall        │
│  ✅ Containment completed in 0.24 seconds — no data loss confirmed     │
└─────────────────────────────────────────────────────────────────────────┘
```

```mermaid
graph LR
    PRED["Model Prediction<br/>(Threat Detected)"] --> SHAP["SHAP Value<br/>Attribution"]
    SHAP --> RANK["Rank Features<br/>by Impact %"]
    RANK --> NLP["Semantic<br/>Translation Layer"]
    NLP --> EXEC["Executive<br/>Briefing"]
    NLP --> SOAR["SOAR<br/>Playbook"]

    style PRED fill:#FCE4EC,stroke:#B71C1C
    style SHAP fill:#E8EAF6,stroke:#283593
    style NLP fill:#FFF3E0,stroke:#E65100
    style EXEC fill:#E0F2F1,stroke:#00695C
    style SOAR fill:#E0F2F1,stroke:#00695C
```

---

### 5. Ethical & Privacy Governance

**The Dilemma:** Continuous deep telemetry monitoring (keystrokes, working hours, web endpoints) borders on invasive surveillance, violating employee trust and international privacy laws (GDPR Article 88).

**Mitigation — Differential Privacy with Ingestion-Layer Pseudonymization:**

```mermaid
graph LR
    RAW["Raw Telemetry<br/>(Contains PII)"] --> STRIP["PII Stripping<br/>& SHA-256 Hashing<br/>(Rotating Salt)"]
    STRIP --> ANON["Anonymized<br/>Behavioral Features"]
    ANON --> ML["ML Model<br/>(No Personal Data)"]

    style RAW fill:#FCE4EC,stroke:#B71C1C
    style STRIP fill:#FFF3E0,stroke:#E65100
    style ANON fill:#E0F2F1,stroke:#00695C
    style ML fill:#E8EAF6,stroke:#283593
```

| Concern | Mitigation | Compliance |
|:---|:---|:---|
| Employee PII exposure | SHA-256 pseudonymization with rotating salt | GDPR Art. 88 |
| Payload content inspection | Content stripped before feature extraction | Data minimization |
| Model memorization risk | Differential privacy noise injection | GDPR Art. 25 |

---

## 📁 Repository Structure

```
AI_Cybersecurity_Capstone/
│
├── code/
│   └── threat_detector_xai.py           # AI detection engine + XAI narrative generator
│
├── docs/
│   └── deliverables/
│       └── AI_Cybersecurity_Threat_Detection_Report.pdf   # Executive PDF report
│
├── generate_cybersecurity_pdf.py         # ReportLab PDF compiler script
└── README.md                             # Project documentation (this file)
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install reportlab
```

### Run the AI Threat Detection & XAI Engine

```bash
cd code
python threat_detector_xai.py
```

**Expected Output:** A complete XAI executive briefing showing threat detection results with SHAP-based plain-language explanations.

### Generate the Submission Report PDF

```bash
python generate_cybersecurity_pdf.py
```

**Output:** `docs/deliverables/AI_Cybersecurity_Threat_Detection_Report.pdf`

---

<div align="center">

---

<img src="https://img.shields.io/badge/Authored_by-Garvit_Sharma-00695C?style=for-the-badge" alt="author"/>&nbsp;&nbsp;<img src="https://img.shields.io/badge/Roll_No-2301730190-1565C0?style=for-the-badge" alt="roll"/>

*Confidential Enterprise Threat Detection System*

</div>
