"""
Utilities Package

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import yaml
from pathlib import Path
from typing import Dict

from .data import (
    generate_incident_data,
    generate_compliance_data,
    generate_system_health,
    get_mock_incidents,
    get_cloud_resources,
    get_control_status,
    get_resource_metrics,
    get_team_metrics,
    get_security_metrics,
    generate_mock_report,
)

from .formatting import (
    format_classification_banner,
    format_footer,
    format_metric_container,
    format_alert,
    format_table,
)

from .logging import LogHandler
from .compliance import ComplianceStatus, ComplianceResult, ComplianceChecker, ReportGenerator


# dashboard/src/utils/__init__.py -> parents: utils, src, dashboard
_DASHBOARD_ROOT = Path(__file__).resolve().parent.parent.parent
_DEFAULT_CONFIG_PATH = _DASHBOARD_ROOT / "config" / "config.yaml"


def load_config(config_path: str | Path = _DEFAULT_CONFIG_PATH) -> Dict:
    """Load configuration from YAML file.

    The default path is resolved relative to this module's own location
    (dashboard/config/config.yaml) rather than the process's current working
    directory, so it works whether the app is launched via
    `cd dashboard/src && streamlit run app.py` (local dev) or
    `streamlit run src/app.py` from /app (the Dockerfile's CMD) — those two
    launch modes have different CWDs, and a CWD-relative default only worked
    for one of them.
    """
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            # Add base path for control files
            config["app"]["base_path"] = str(Path(config_path).parent)
        return config
    except Exception as e:
        raise Exception(f"Error loading configuration: {str(e)}")


__all__ = [
    # Data generation functions
    "generate_incident_data",
    "generate_compliance_data",
    "generate_system_health",
    "get_mock_incidents",
    "get_cloud_resources",
    "get_control_status",
    "get_resource_metrics",
    "get_team_metrics",
    "get_security_metrics",
    "generate_mock_report",
    # Formatting functions
    "format_classification_banner",
    "format_footer",
    "format_metric_container",
    "format_alert",
    "format_table",
    # Configuration
    "load_config",
    # Logging
    "LogHandler",
    # Compliance
    "ComplianceStatus",
    "ComplianceResult",
    "ComplianceChecker",
    "ReportGenerator",
]
