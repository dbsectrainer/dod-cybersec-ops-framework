# Copilot Instructions for DoD Cybersecurity Operations & Incident Response Framework

## Project Overview
- This is a multi-cloud cybersecurity framework for DoD agencies, integrating DevSecOps, incident response, and compliance automation.
- Major components: Zero Trust Security Layer, Multi-Cloud Infrastructure (AWS GovCloud, Azure Government, Platform One), Security Operations (SOC, threat hunting, automated response), and Compliance Management.
- Architecture and workflows are documented in `docs/architecture/`, `docs/diagrams/`, and referenced in the main `README.md`.

## Key Developer Workflows
- **Dashboard App:** Main entry is `dashboard/src/app.py` (Streamlit). Run with:
  ```bash
  cd dashboard/src
  streamlit run app.py
  ```
- **Environment Setup:**
  - Use Python 3.12+ and create a virtual environment in `dashboard/`.
  - Install dependencies from root `requirements.txt` (runtime) and `dashboard/requirements-dev.txt` (lint/type-check/test tooling).
- **Configuration:**
  - Configuration is in `dashboard/config/config.yaml`.
  - Cloud credentials and authentication must be configured before running in production.
- **Testing:**
  - Basic syntax check: `python -m py_compile dashboard/src/app.py`
  - Code quality: `ruff check dashboard/src/`, `ruff format --check dashboard/src/`, and `mypy dashboard/src/`
  - Tests: `pytest dashboard/tests/`
- **Containerization:**
  - Build from the repo root (context must include both the root
    `requirements.txt` and the `dashboard/` subtree):
    `docker build -f dashboard/Dockerfile -t dod-cybersec-dashboard .`
  - Without Iron Bank registry access, add
    `--build-arg BASE_IMAGE=python:3.12-slim`.

## Project-Specific Patterns & Conventions
- **Classification Markings:** All files must include DoD classification headers.
- **Authentication:** PIV/CAC, MFA, and RBAC are required; see `dashboard/src/auth/` for implementation.
- **Compliance Controls:** Controls are defined in YAML under `dashboard/config/controls/` (e.g., `rmf_controls.yaml`, `stig_controls.yaml`).
- **Monitoring & Metrics:** Prometheus and Grafana are configured via YAML in `dashboard/config/grafana/` and `dashboard/config/prometheus/`.
- **Incident Response:** Playbooks and workflows are documented in `docs/operations/` and `docs/diagrams/incident_response.mmd`.
- **Logging:** Use centralized logging and audit trails as described in `dashboard/README.md` and technical docs.

## Integration Points
- **Cloud Providers:** Integrate with AWS GovCloud, Azure Government, and Platform One. Configuration details in `dashboard/config/` and `docs/technical/`.
- **Security Tools:** SIEM, EDR/XDR, SOAR integrations are described in `docs/technical/` and implemented in `dashboard/src/utils/`.
- **Compliance Mapping:** Regulatory frameworks (NIST, DISA STIG, CNSS) are mapped in `docs/compliance/` and YAML controls.

## Examples
- To add a new compliance control, update the relevant YAML in `dashboard/config/controls/` and ensure it is loaded in `dashboard/src/utils/compliance.py`.
- For new authentication methods, extend `dashboard/src/auth/` and update configuration in `dashboard/config/config.yaml`.
- For new metrics, add Prometheus rules in `dashboard/config/prometheus/rules/` and dashboards in `dashboard/config/grafana/provisioning/dashboards/`.

## References
- Architecture diagrams: `docs/diagrams/`
- Technical specs: `docs/technical/`
- Compliance docs: `docs/compliance/`
- Operations/playbooks: `docs/operations/`

---

**Last updated:** September 22, 2026

> If any section is unclear or missing, please provide feedback for iterative improvement.
