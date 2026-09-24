"""
Unit tests for compliance utilities.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

from utils.compliance import ComplianceChecker, ComplianceStatus, ReportGenerator


def test_compliance_checker_loads_frameworks(config):
    checker = ComplianceChecker(config)
    assert "NIST RMF" in checker.controls
    assert "DISA STIG" in checker.controls


def test_compliance_checker_returns_results(config):
    checker = ComplianceChecker(config)
    results = checker.check_compliance("NIST RMF")

    assert len(results) > 0
    assert all(result.framework == "NIST RMF" for result in results)
    assert all(isinstance(result.status, ComplianceStatus) for result in results)


def test_report_generator_adds_classification_markings(config):
    generator = ReportGenerator(config)
    marked = generator._add_classification_markings({"sample": "data"})

    assert marked["classification"] == config["app"]["classification"]
    assert marked["header"] is True
    assert marked["footer"] is True
    assert marked["watermark"] is True
    assert marked["data"] == {"sample": "data"}
