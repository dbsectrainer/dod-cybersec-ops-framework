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
    generate_mock_report
)

from .formatting import (
    format_classification_banner,
    format_footer,
    format_metric_container,
    format_alert,
    format_table
)

from .logging import LogHandler
from .compliance import (
    ComplianceStatus,
    ComplianceResult,
    ComplianceChecker,
    ReportGenerator
)

def load_config(config_path: str = "../config/config.yaml") -> Dict:
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            # Add base path for control files
            config['app']['base_path'] = str(Path(config_path).parent)
        return config
    except Exception as e:
        raise Exception(f"Error loading configuration: {str(e)}")

__all__ = [
    # Data generation functions
    'generate_incident_data',
    'generate_compliance_data',
    'generate_system_health',
    'get_mock_incidents',
    'get_cloud_resources',
    'get_control_status',
    'get_resource_metrics',
    'get_team_metrics',
    'get_security_metrics',
    'generate_mock_report',
    
    # Formatting functions
    'format_classification_banner',
    'format_footer',
    'format_metric_container',
    'format_alert',
    'format_table',
    
    # Configuration
    'load_config',
    
    # Logging
    'LogHandler',
    
    # Compliance
    'ComplianceStatus',
    'ComplianceResult',
    'ComplianceChecker',
    'ReportGenerator'
]
