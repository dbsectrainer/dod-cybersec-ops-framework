# DoD Cybersecurity Operations Dashboard

**Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)**

## Overview

This dashboard provides real-time monitoring and visualization of the DoD Cybersecurity Operations and Incident Response Framework. It integrates data from multiple cloud environments and security tools to provide a comprehensive view of the security posture.

## Features

- Real-time security operations monitoring
- Compliance status tracking
- System health monitoring
- Incident response management
- Asset management
- Automated compliance reporting

## Prerequisites

- Python 3.12+
- Streamlit
- AWS GovCloud Access
- Azure Government Access
- Platform One Access
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd dod-cybersec-ops-framework/dashboard
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r ../requirements.txt
```

4. Configure environment:
```bash
cp config/config.yaml.example config/config.yaml
# Edit config.yaml with your settings
```

## Running the Dashboard

1. Start the Streamlit server:
```bash
cd src
streamlit run app.py
```

2. Access the dashboard:
```
http://localhost:8501
```

## Security Controls

### Authentication
- PIV/CAC integration
- Multi-factor authentication
- Role-based access control
- Session management

### Data Protection
- Data encryption at rest and in transit
- Classification validation
- Data sanitization
- Access logging

### Compliance
- DISA STIG compliance
- NIST RMF controls
- Zero Trust implementation
- Continuous monitoring

## Directory Structure

```
dashboard/
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── auth/               # Authentication modules (PIV/CAC, session management)
│   └── utils/              # Utility functions (compliance, data processing, logging)
├── config/
│   ├── config.yaml         # Configuration settings
│   └── config.yaml.example # Example configuration
├── data/
│   ├── metrics/           # Metrics data
│   └── reports/           # Generated reports
├── tests/
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
└── docs/                 # Documentation
```

## Development

### Setting Up Development Environment

1. Install development dependencies (includes runtime deps via `-r ../requirements.txt`):
```bash
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Run unit tests
pytest tests/unit

# Run integration tests
pytest tests/integration

# Run with coverage
pytest --cov=src tests/
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Document all functions and classes
- Add classification markings to all files

## Deployment

### Production Deployment

1. Build container:
```bash
docker build -t dod-cybersec-dashboard .
```

2. Deploy to Platform One:
```bash
# Follow Platform One deployment procedures
```

### Configuration

1. Set up cloud credentials
2. Configure authentication
3. Set up monitoring
4. Enable logging

## Monitoring

### Metrics
- Dashboard performance
- User activity
- System health
- API usage

### Logging
- Application logs
- Security events
- Audit trails
- Error tracking

## Support

### Contact Information
- Security Team: [CONTACT INFO]
- Development Team: [CONTACT INFO]
- Operations Team: [CONTACT INFO]

### Reporting Issues
- Security issues: Follow security policy
- Bug reports: Use issue template
- Feature requests: Use feature template

## Contributing

See CONTRIBUTING.md for guidelines.

## Security

See SECURITY.md for security policy and procedures.

## License

This project is licensed under DoD Open Source Agreement Version 1.0.

## Distribution Statement

DISTRIBUTION STATEMENT D. Distribution authorized to the Department of Defense and U.S. DoD contractors only; Administrative/Operational Use; DATE. Other requests shall be referred to [APPROPRIATE AUTHORITY].

Last Updated: January 27, 2025
