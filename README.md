# DoD Cybersecurity Operations Framework

> Comprehensive DoD cybersecurity operations and incident response framework for multi-cloud DevSecOps environments, aligned to DoD 8140 and NIST RMF.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/) [![DoD 8140](https://img.shields.io/badge/DoD-8140-darkgreen.svg)](https://public.cyber.mil/workforce/) [![NIST RMF](https://img.shields.io/badge/NIST-RMF-darkblue.svg)](https://csrc.nist.gov/projects/risk-management) [![FedRAMP Moderate](https://img.shields.io/badge/FedRAMP-Moderate-orange.svg)](https://www.fedramp.gov/) [![License: DoD-OSA-1.0](https://img.shields.io/badge/license-DoD--OSA--1.0-lightgrey.svg)](LICENSE)

---

## Overview

1. Implements a Zero Trust security layer with PIV/CAC authentication, role-based access control, continuous verification, and micro-segmentation across multi-cloud government environments.
2. Provides a Streamlit-based Security Operations dashboard for 24/7 SOC monitoring, automated incident response, threat hunting, and compliance status visualization.
3. Integrates with AWS GovCloud, Azure Government, Platform One, and milCloud 2.0 for a unified multi-cloud security posture.
4. Enforces compliance with DoD 8140, NIST SP 800-53 Rev 5, DISA STIGs, and the DoD Enterprise DevSecOps Reference Design through automated control validation.
5. Embeds a secure CI/CD pipeline with container security scanning, automated testing, and compliance validation gates at every stage of the software delivery lifecycle.
6. Delivers structured operational documentation covering architecture, compliance controls, incident response playbooks, and standard operating procedures for DoD agency adoption.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Zero Trust Security Layer                   │
│         PIV/CAC Auth │ RBAC │ Continuous Verification           │
│                     Micro-segmentation                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│               Multi-Cloud Government Infrastructure             │
│    ┌──────────────┐  ┌───────────────┐  ┌──────────────────┐   │
│    │  AWS GovCloud│  │ Azure Gov     │  │  milCloud 2.0    │   │
│    │  (East/West) │  │ (DoD IL5)     │  │  Platform One    │   │
│    └──────────────┘  └───────────────┘  └──────────────────┘   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Security Operations Center                     │
│     24/7 SOC │ SIEM/Splunk │ EDR/XDR │ SOAR │ Threat Hunting   │
│              Prometheus + Grafana + ELK Stack                   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DevSecOps Pipeline                           │
│    Source → SAST/DAST → Container Scan → Compliance Gate       │
│                  → Deploy → Runtime Monitoring                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Audit & Compliance Logger                      │
│     NIST RMF │ DoD 8140 │ DISA STIGs │ CNSS │ Control Tracking │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Features

### Zero Trust Security

The framework implements a full Zero Trust architecture aligned to NIST SP 800-207 and the DoD Zero Trust Reference Architecture, enforcing continuous verification at every layer.

- PIV/CAC integration for strong identity assurance at all access points
- Role-based access control (RBAC) with least-privilege enforcement
- Micro-segmentation of workloads across multi-cloud environments
- Continuous session verification with configurable timeout policies
- DoD system-use notification banners and audit logging on every login event

### Multi-Cloud Infrastructure

| Cloud Platform | Classification Level | Key Services |
| --- | --- | --- |
| AWS GovCloud | IL2–IL5 | S3, EC2, Lambda, GuardDuty |
| Azure Government | IL4–IL5 | AKS, Key Vault, Sentinel |
| Platform One | IL2–IL6 | Big Bang, Ironbank |
| milCloud 2.0 | IL6 | On-prem workloads |

Integration libraries for AWS (boto3) and Azure (azure-identity, azure-mgmt-resource) are included in requirements, enabling unified cloud resource visibility from a single dashboard.

### Security Operations Center

The included Streamlit dashboard (`dashboard/src/app.py`) delivers a real-time SOC interface covering:

- Live incident tracking with priority classification and assignment workflows
- Automated response runbooks triggered by SIEM alert thresholds
- Threat hunting dashboards designed for Elasticsearch/OpenSearch-backed data (the client libraries are bundled; standing up an Elasticsearch/OpenSearch service is not currently included in `docker-compose.yml`)
- System health monitoring via Prometheus and Grafana with pre-configured alert rules
- Exportable compliance and incident reports for leadership review

### DevSecOps Integration

The pipeline architecture enforces security gates at every stage of software delivery:

- Static (SAST) and dynamic (DAST) analysis before any artifact promotion
- Container image scanning with policy enforcement via Ironbank-compatible registries
- Automated compliance validation against NIST controls and DISA STIGs in CI
- Secrets management via HashiCorp Vault with policy-as-code (HCL)
- Docker Compose and Kubernetes-ready deployment manifests under `dashboard/`

### Security & Compliance

- DoD 8140 workforce certification alignment (IAT/IAM/CSSP roles; DoD 8140 supersedes the legacy DoD 8570.01-M manual)
- NIST SP 800-53 Rev 5 control families with automated tracking
- DISA Security Technical Implementation Guides (STIGs)
- CNSS directives integration
- DoD Enterprise DevSecOps Reference Design
- DoD Cloud Computing Security Requirements Guide (SRG)
- Risk Management Framework (RMF) lifecycle support (Categorize → Select → Implement → Assess → Authorize → Monitor)

---

## Quick Start

### Prerequisites

- Python 3.12+
- Docker and Docker Compose (for containerized deployment)
- Kubernetes 1.31+ (for production cluster deployment)
- HashiCorp Vault 1.18+ (for secrets management; OpenBao is an Apache-2.0 alternative)
- Access to a DoD-authorized cloud environment (AWS GovCloud, Azure Government, or milCloud 2.0)

### Local Development

```bash
# Clone the repository
git clone https://github.com/dbsectrainer/dod-cybersec-ops-framework.git
cd dod-cybersec-ops-framework

# Install Python dependencies
pip install -r requirements.txt

# Configure dashboard secrets from the template
# (dashboard/src/.streamlit/secrets.toml is a symlink to this file)
cp dashboard/.streamlit/secrets.toml.example dashboard/.streamlit/secrets.toml
# Edit dashboard/.streamlit/secrets.toml with your environment-specific values

# Launch the Streamlit dashboard
cd dashboard/src
streamlit run app.py
```

The dashboard will be available at `http://localhost:8501`. A DoD system-use banner and authentication prompt will appear on first load.

### Docker Deployment

```bash
# Start the supporting services (Prometheus + Grafana + Vault + exporters)
cd dashboard
cp .env.example .env  # then edit with real values
docker compose up -d

# Verify all containers are running
docker compose ps

# The dashboard app itself is a separate image (docker-compose.yml doesn't
# build/run it yet — see docs/ROADMAP.md). Build and run it directly.
# secrets.toml is deliberately excluded from the image (see .dockerignore),
# so it must be mounted at runtime:
cd ..
docker build -f dashboard/Dockerfile -t dod-cybersec-dashboard .
docker run -p 8501:8501 --env-file dashboard/.env \
  -v "$(pwd)/dashboard/.streamlit/secrets.toml:/app/.streamlit/secrets.toml:ro" \
  dod-cybersec-dashboard
```

Prometheus is available at `http://localhost:9090`, Grafana at `http://localhost:3000`.

### Configuration

- Dashboard config: `dashboard/config/config.yaml`
- RMF controls: `dashboard/config/controls/rmf_controls.yaml`
- STIG controls: `dashboard/config/controls/stig_controls.yaml`
- Alertmanager rules: `dashboard/config/alertmanager/alertmanager.yml`
- Prometheus rules: `dashboard/config/prometheus/rules/sample_rules.yml`
- Vault policy: `dashboard/config/vault/policies/sample_policy.hcl`

---

## Production Ready Status

**Framework and Dashboard Verified for DoD Development Environments**

- Zero Trust authentication module implemented with PIV/CAC support and session management
- Streamlit SOC dashboard with incident tracking, compliance views, and system health monitoring
- Docker Compose stack with Prometheus, Grafana, Alertmanager, and HashiCorp Vault integration
- RMF and STIG control configuration files present and structured for environment-specific population
- Python dependency stack pinned with security-relevant packages (python-jose, bcrypt, passlib)
- Compliance utilities (`dashboard/src/utils/compliance.py`) for automated control status evaluation
- Structured logging module (`dashboard/src/utils/logging.py`) for audit-trail generation
- Comprehensive documentation under `docs/` covering architecture, compliance, operations, and technical implementation

### Verification

```bash
# Install dependencies
pip install -r requirements.txt

# Run linter
flake8 dashboard/src/

# Run type checker
mypy dashboard/src/

# Run tests
pytest

# Start dashboard (expected: Streamlit server on port 8501)
cd dashboard/src && streamlit run app.py
```

Expected output on successful startup:

```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

---

## Project Structure

```
dod-cybersec-ops-framework/
├── dashboard/
│   ├── .streamlit/
│   │   └── secrets.toml
│   ├── config/
│   │   ├── alertmanager/
│   │   ├── controls/
│   │   │   ├── rmf_controls.yaml
│   │   │   └── stig_controls.yaml
│   │   ├── grafana/
│   │   ├── prometheus/
│   │   └── vault/
│   ├── src/
│   │   ├── app.py
│   │   ├── auth/
│   │   │   ├── banner.py
│   │   │   ├── login.py
│   │   │   └── session.py
│   │   └── utils/
│   │       ├── compliance.py
│   │       ├── data.py
│   │       ├── formatting.py
│   │       └── logging.py
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   ├── architecture/
│   │   ├── application/
│   │   ├── network/
│   │   └── security/
│   ├── compliance/
│   ├── diagrams/
│   ├── operations/
│   ├── technical/
│   ├── ENTERPRISE.md
│   └── ROADMAP.md
├── requirements.txt
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── README.md
```

---

## BE EASY ENTERPRISES Federal Portfolio

| Showcase Project | Repository | Description |
| --- | --- | --- |
| **Secure RAG Pipeline** | [Secure-Generative-AI-Platform-on-AWS](https://github.com/dbsectrainer/Secure-Generative-AI-Platform-on-AWS) | AWS Bedrock + RAG with FedRAMP High alignment |
| **DevSecOps CI/CD** | **[dod-cybersec-ops-framework](https://github.com/dbsectrainer/dod-cybersec-ops-framework)** | **This repo** |
| **Zero Trust Architecture** | [AEGIS](https://github.com/dbsectrainer/AEGIS) | FedRAMP High + NIST 800-207 Zero Trust |
| **FedRAMP Control Automation** | [nist_800_53_scanner](https://github.com/dbsectrainer/nist_800_53_scanner) | NIST 800-53 Rev 5 compliance scanner |
| **Federal AI Governance** | [ai-safety-governance](https://github.com/dbsectrainer/ai-safety-governance) | EO 14110 / OMB M-24-10 aligned |
| **CMMC 2.0 Dashboard** | [integrated-cyber-risk-compliance](https://github.com/dbsectrainer/integrated-cyber-risk-compliance) | CMMC 2.0 readiness assessment |
| **FedRAMP 30-Day Guide** | [cloud-security-best-practices](https://github.com/dbsectrainer/cloud-security-best-practices) | Day-by-day FedRAMP implementation roadmap |
| **Agentic AI Workflow** | [federal-doc-triage-agent](https://github.com/dbsectrainer/federal-doc-triage-agent) | Production-ready LangGraph + Bedrock triage agent |

---

## Author

**Donnivis Baker** — [github.com/dbsectrainer](https://github.com/dbsectrainer)
**BE EASY ENTERPRISES** — Federal IT Modernization & Cybersecurity

For questions, partnerships, or federal engagement inquiries, open an issue or reach out directly.

**Document Version:** 1.1 | **Last Updated:** 2026-09-22 | **DoD 8140:** IAT/IAM Level II+
