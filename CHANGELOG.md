# Changelog

**Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)**

All notable changes to the DoD Cybersecurity Operations and Incident Response Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-22

### Changed
- Bumped Python floor from EOL 3.9 to 3.12 across the Dockerfile, READMEs,
  and CI; added upper-bound pins to `requirements.txt` and split dev/lint/
  test tooling into `dashboard/requirements-dev.txt` (ruff + mypy replace
  black + flake8)
- Pinned every floating `:latest` Docker image tag in `docker-compose.yml`
  and bumped HashiCorp Vault; moved Grafana/Vault dev-mode credentials to
  a gitignored `.env` (see `.env.example`)
- Bumped documented Kubernetes/Istio/Vault/Elastic Stack version floors to
  current supported lines
- Reworded DoD 8570 references to DoD 8140 (its successor directive)
  throughout the docs
- Reconciled conflicting compliance claims (license badge, FedRAMP level,
  AWS GovCloud Impact Level) to the more conservative, defensible value
  pending confirmation against an actual authorization package

### Fixed
- Deleted `dashboard/src/utils.py`, a dead/broken duplicate of the already-
  migrated `utils/` package that raised `NameError` on import
- Fixed `session.py`/`login.py` hardcoding session-timeout and password-
  length values instead of reading them from `config.yaml`
- Fixed two `st.date_input` tuple-indexing bugs in `app.py` (caught by
  adding mypy to CI)
- Replaced committed demo secrets with placeholders, added
  `secrets.toml.example`, gitignored the real file, and fixed a symlink
  that pointed at an absolute local dev machine path
- Removed 10 stray compiled `.pyc` files that had been committed to git

### Added
- `.github/workflows/ci.yml`: lint, format check, type-check, test, and
  Docker build validation on every push/PR
- `dashboard/tests/` with a smoke-test suite (previously referenced but
  nonexistent)
- Previously-missing but referenced `config.yaml.example` and compliance
  scanner stub configs

## [1.0.0] - 2025-01-27

### Added
- Initial framework documentation
- Enterprise architecture documentation
- Comprehensive documentation structure:
  - Architecture documentation
  - Compliance documentation
  - Operations documentation
  - Technical documentation
- Security documentation:
  - Security policy
  - Contributing guidelines
  - Code of conduct
- Directory structure for implementation documents
- Multi-cloud implementation guidance
- DevSecOps pipeline documentation
- Security controls documentation
- Compliance requirements
- Operational procedures
- Technical specifications

### Security
- FOUO classification markings
- Security policy implementation
- Access control documentation
- Incident response procedures
- Vulnerability management process

### Documentation
- README.md with project overview
- ENTERPRISE.md with architecture details
- Architecture documentation structure
- Compliance documentation structure
- Operations documentation structure
- Technical documentation structure

## [Unreleased]

### Security Enhancements
- Enhanced Zero Trust Architecture implementation
- Advanced threat detection capabilities
- Improved incident response procedures
- Enhanced compliance monitoring

### Cloud Integration
- Additional cloud provider integration
- Enhanced container security
- Improved cloud security controls
- Advanced monitoring capabilities

### DevSecOps Pipeline
- Enhanced security scanning
- Automated compliance checks
- Improved CI/CD security
- Container hardening procedures

### Documentation
- Additional implementation guides
- Enhanced security procedures
- Updated compliance requirements
- Expanded technical specifications

## Version Guidelines

### Version Format
- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality
- PATCH version for backwards-compatible bug fixes

### Security Considerations
- All security-related changes must be documented
- Impact assessment required for security changes
- Compliance verification for all updates
- Security review for all releases

### Documentation Updates
- All changes must be documented
- Classification markings maintained
- Security implications noted
- Compliance requirements updated

## Release Process

### Requirements
1. Security review completed
2. Compliance verification
3. Documentation updated
4. Tests passing
5. Approvals obtained

### Procedures
1. Version number updated
2. Changelog updated
3. Security review conducted
4. Release notes prepared
5. Deployment executed

## Additional Information

### Contact
- Security Team: [CONTACT INFO]
- Compliance Team: [CONTACT INFO]
- Development Team: [CONTACT INFO]

### References
- DoD Security Guidelines
- NIST Standards
- DISA STIGs
- Compliance Requirements
