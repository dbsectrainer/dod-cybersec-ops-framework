"""
Utility functions for the DoD Cybersecurity Operations Dashboard

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import yaml
import logging
import boto3
import azure.identity
import azure.mgmt.security
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config(config_path: str = "../config/config.yaml") -> Dict:
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logger.info("Configuration loaded successfully")
        return config
    except Exception as e:
        logger.error(f"Error loading configuration: {str(e)}")
        raise

def setup_aws_client(service: str, region: str = "us-gov-west-1") -> Any:
    """Setup AWS client for specified service."""
    try:
        session = boto3.Session(region_name=region)
        client = session.client(service)
        logger.info(f"AWS {service} client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Error setting up AWS client: {str(e)}")
        raise

def setup_azure_client() -> Any:
    """Setup Azure client for security operations."""
    try:
        credential = azure.identity.DefaultAzureCredential()
        client = azure.mgmt.security.SecurityCenter(credential)
        logger.info("Azure security client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Error setting up Azure client: {str(e)}")
        raise

def get_compliance_status(framework: str) -> Dict:
    """Get compliance status for specified framework."""
    try:
        # Mock compliance data - replace with actual implementation
        compliance_data = {
            'total_controls': 400,
            'implemented': 342,
            'in_progress': 48,
            'not_started': 10,
            'last_updated': datetime.now(timezone.utc)
        }
        logger.info(f"Retrieved compliance status for {framework}")
        return compliance_data
    except Exception as e:
        logger.error(f"Error getting compliance status: {str(e)}")
        raise

def get_security_metrics() -> Dict:
    """Get security metrics from various sources."""
    try:
        # Mock security metrics - replace with actual implementation
        metrics = {
            'incidents': {
                'critical': 2,
                'high': 5,
                'medium': 8,
                'low': 15
            },
            'alerts': {
                'total': 150,
                'new': 12,
                'in_progress': 8,
                'resolved': 130
            },
            'response_time': {
                'average': 15,  # minutes
                'critical': 5,
                'high': 10,
                'medium': 20,
                'low': 30
            }
        }
        logger.info("Retrieved security metrics successfully")
        return metrics
    except Exception as e:
        logger.error(f"Error getting security metrics: {str(e)}")
        raise

def get_system_health() -> Dict:
    """Get system health metrics."""
    try:
        # Mock system health data - replace with actual implementation
        health_data = {
            'services': {
                'aws': 99.99,
                'azure': 99.95,
                'platform_one': 99.98,
                'milcloud': 99.90
            },
            'resources': {
                'cpu': 45,
                'memory': 62,
                'storage': 78,
                'network': 25
            }
        }
        logger.info("Retrieved system health metrics successfully")
        return health_data
    except Exception as e:
        logger.error(f"Error getting system health: {str(e)}")
        raise

def generate_report(report_type: str, start_date: datetime, end_date: datetime) -> bytes:
    """Generate compliance or security report."""
    try:
        # Mock report generation - replace with actual implementation
        report_data = f"Mock report data for {report_type} from {start_date} to {end_date}"
        logger.info(f"Generated {report_type} report successfully")
        return report_data.encode()
    except Exception as e:
        logger.error(f"Error generating report: {str(e)}")
        raise

def validate_classification(data: Any) -> bool:
    """Validate data classification markings."""
    try:
        if isinstance(data, (str, bytes)):
            return "UNCLASSIFIED" in str(data) and "FOUO" in str(data)
        return True
    except Exception as e:
        logger.error(f"Error validating classification: {str(e)}")
        return False

def sanitize_data(data: Any) -> Any:
    """Sanitize data for display."""
    try:
        if isinstance(data, str):
            # Remove any potentially sensitive information
            sanitized = data.replace('\n', ' ').strip()
            return sanitized[:1000]  # Limit length
        return data
    except Exception as e:
        logger.error(f"Error sanitizing data: {str(e)}")
        return None

def format_timestamp(timestamp: datetime) -> str:
    """Format timestamp for display."""
    try:
        return timestamp.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        logger.error(f"Error formatting timestamp: {str(e)}")
        return str(timestamp)

def calculate_metrics(data: pd.DataFrame) -> Dict:
    """Calculate security and performance metrics."""
    try:
        metrics = {
            'mean': data.mean(),
            'median': data.median(),
            'std': data.std(),
            'min': data.min(),
            'max': data.max()
        }
        logger.info("Calculated metrics successfully")
        return metrics
    except Exception as e:
        logger.error(f"Error calculating metrics: {str(e)}")
        raise

def validate_config(config: Dict) -> bool:
    """Validate configuration settings."""
    try:
        required_keys = ['app', 'security', 'datasources', 'monitoring']
        return all(key in config for key in required_keys)
    except Exception as e:
        logger.error(f"Error validating config: {str(e)}")
        return False
