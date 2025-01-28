"""
Utilities Package

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

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
    'format_table'
]
