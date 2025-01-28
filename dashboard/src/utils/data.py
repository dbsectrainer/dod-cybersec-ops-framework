"""
Data Generation and Management Module

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_incident_data():
    """Generate mock incident trend data."""
    dates = pd.date_range(start='2025-01-01', end='2025-01-27', freq='D')
    incidents = np.random.randint(1, 20, size=len(dates))
    return pd.DataFrame({'Date': dates, 'Incidents': incidents})

def generate_compliance_data():
    """Generate mock compliance metrics data."""
    categories = ['STIG', 'RMF', 'Zero Trust', 'Cloud Security']
    compliance = np.random.uniform(70, 100, size=len(categories))
    return pd.DataFrame({'Category': categories, 'Compliance': compliance})

def generate_system_health():
    """Generate mock system health metrics."""
    services = ['AWS', 'Azure', 'Platform One', 'milCloud 2.0']
    availability = np.random.uniform(98, 100, size=len(services))
    return pd.DataFrame({'Service': services, 'Availability': availability})

def get_mock_incidents():
    """Get mock active incidents data."""
    return pd.DataFrame({
        'ID': ['INC-001', 'INC-002', 'INC-003'],
        'Severity': ['High', 'Medium', 'Critical'],
        'Status': ['In Progress', 'Under Investigation', 'Containment'],
        'Time': ['2h 15m', '45m', '4h 30m']
    })

def get_cloud_resources():
    """Get mock cloud resource distribution data."""
    return {
        'AWS GovCloud': 150,
        'Azure Government': 120,
        'Platform One': 80,
        'milCloud 2.0': 50
    }

def get_control_status():
    """Get mock control implementation status."""
    return {
        'implemented': {'value': '342/400', 'percentage': '85.5%'},
        'in_progress': {'value': '48/400', 'percentage': '12%'},
        'not_started': {'value': '10/400', 'percentage': '2.5%'}
    }

def get_resource_metrics():
    """Get mock resource utilization metrics."""
    return {
        'cpu': {'value': '45%', 'delta': '-5%'},
        'memory': {'value': '62%', 'delta': '3%'},
        'storage': {'value': '78%', 'delta': '2%'}
    }

def get_team_metrics():
    """Get mock response team metrics."""
    return {
        'available_teams': {'value': '3/4', 'delta': '-1'},
        'response_time': {'value': '15 min', 'delta': '-2 min'},
        'open_tickets': {'value': '5', 'delta': '+2'}
    }

def get_security_metrics():
    """Get mock security status metrics."""
    return {
        'compliant_systems': {'value': '385/400', 'percentage': '96.25%'},
        'patch_status': {'value': '398/400', 'percentage': '99.5%'},
        'security_findings': {'value': '12', 'delta': '-3'}
    }

def generate_mock_report(report_type, start_date, end_date):
    """Generate a mock compliance report."""
    return f"""
    DoD Cybersecurity Operations Framework
    {report_type} Report
    Period: {start_date} to {end_date}
    
    This is a mock report for demonstration purposes.
    Classification: UNCLASSIFIED // FOUO
    """
