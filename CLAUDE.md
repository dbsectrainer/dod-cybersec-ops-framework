# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Department of Defense Cybersecurity Operations and Incident Response Framework - a comprehensive cybersecurity framework for DoD agencies implementing DevSecOps in multi-cloud environments. The project adheres to DoD 8570 directives and integrates with NIST RMF, CNSS, and DoD Enterprise DevSecOps Reference Design.

## Core Architecture

The framework consists of four main components:

1. **Zero Trust Security Layer**: PIV/CAC integration, RBAC, continuous verification, micro-segmentation
2. **Multi-Cloud Infrastructure**: AWS GovCloud, Azure Government, Platform One, milCloud 2.0
3. **Security Operations**: 24/7 SOC operations, automated response, threat hunting, incident management
4. **DevSecOps Integration**: Secure CI/CD pipeline, container security, automated testing, compliance validation

## Key Commands

### Dashboard Application
```bash
# Set up development environment
cd dashboard
python -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r ../requirements.txt

# Configure application (copy and edit from existing config)
# Edit config/config.yaml with your settings

# Run the dashboard
cd src
streamlit run app.py
# Access at http://localhost:8501
```

### Testing
```bash
# Basic syntax check
python -m py_compile dashboard/src/app.py

# Code quality checks (if tests are implemented)
# pytest dashboard/tests/unit
# pytest dashboard/tests/integration
# pytest --cov=src dashboard/tests/
```

### Code Quality
```bash
# Code formatting
black dashboard/src/

# Linting
flake8 dashboard/src/

# Type checking
mypy dashboard/src/
```

### Containerization
```bash
# Build Docker image
cd dashboard
docker build -t dod-cybersec-dashboard .

# Run with docker-compose (includes Prometheus, Grafana, etc.)
docker-compose up -d
```

## Security & Compliance Requirements

- **Classification**: All files must include DoD classification markings (UNCLASSIFIED // FOUO)
- **Authentication**: PIV/CAC integration and multi-factor authentication required
- **Access Control**: Role-based access control (RBAC) implementation
- **Compliance**: NIST SP 800-53 Rev 5, DoD Cloud Computing SRG, DISA STIGs compliance
- **Data Protection**: Encryption at rest and in transit, audit logging

## Directory Structure

```
dashboard/
├── src/
│   ├── app.py              # Main Streamlit application entry point
│   ├── auth/               # Authentication modules (PIV/CAC, session management)
│   └── utils/              # Utilities (compliance, data processing, logging)
├── config/
│   ├── controls/           # Compliance controls (RMF, STIG YAML definitions)
│   ├── grafana/            # Grafana dashboards and datasource configs
│   ├── prometheus/         # Prometheus configuration and alerting rules
│   ├── alertmanager/       # AlertManager configuration
│   └── config.yaml         # Main dashboard configuration
├── .streamlit/             # Streamlit configuration
└── docker-compose.yml      # Multi-service development environment
```

## Development Patterns

- **Configuration**: Use YAML files in `dashboard/config/` for all configuration
- **Compliance Controls**: Define controls in `dashboard/config/controls/` and load via `utils/compliance.py`
- **Authentication**: Extend `dashboard/src/auth/` for new auth methods
- **Monitoring**: Add Prometheus rules in `config/prometheus/rules/` and Grafana dashboards in `config/grafana/`
- **Cloud Integration**: AWS GovCloud, Azure Government, and Platform One integrations in `src/utils/`

## Integration Points

- **Multi-Cloud**: Configured for AWS GovCloud, Azure Government, Platform One
- **Security Tools**: SIEM, EDR/XDR, SOAR platform integrations
- **Monitoring Stack**: Prometheus, Grafana, ELK Stack, Splunk Enterprise
- **Container Platform**: Kubernetes 1.24+, Istio Service Mesh 1.18+
- **Secret Management**: HashiCorp Vault 1.12+

## Documentation References

- Architecture diagrams: `docs/diagrams/` (Mermaid format)
- Technical implementation: `docs/technical/`
- Compliance documentation: `docs/compliance/`
- Operations runbooks: `docs/operations/`
- Enterprise architecture: `docs/ENTERPRISE.md`