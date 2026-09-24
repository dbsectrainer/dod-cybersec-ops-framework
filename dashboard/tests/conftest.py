"""
Shared pytest fixtures for dashboard tests.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "dashboard" / "config" / "config.yaml"


@pytest.fixture
def config() -> dict:
    """Load the dashboard configuration with base_path set."""
    with open(CONFIG_PATH) as file:
        loaded = yaml.safe_load(file)
    loaded["app"]["base_path"] = str(CONFIG_PATH.parent)
    return loaded


@pytest.fixture
def log_config(tmp_path) -> dict:
    """Minimal logging configuration for unit tests."""
    return {
        "logging": {
            "level": "INFO",
            "format": "%(levelname)s - %(message)s",
            "handlers": {
                "file": {
                    "filename": str(tmp_path / "dashboard.log"),
                    "max_size": 1048576,
                    "backup_count": 2,
                },
                "syslog": {"enabled": False, "facility": "local0"},
            },
        }
    }
