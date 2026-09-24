"""
Unit tests for logging utilities.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

from pathlib import Path

from utils.logging import LogHandler


def test_log_handler_creates_log_file(log_config):
    handler = LogHandler(log_config)
    log_path = Path(log_config["logging"]["handlers"]["file"]["filename"])

    handler.logger.info("test security event")
    assert log_path.exists()
    assert log_path.stat().st_size > 0


def test_log_handler_backup_logs(log_config):
    handler = LogHandler(log_config)
    log_path = Path(log_config["logging"]["handlers"]["file"]["filename"])
    handler.logger.info("entry before backup")

    handler.backup_logs()

    backup_dir = log_path.parent / "backups"
    backups = list(backup_dir.glob("dashboard_logs_*.log"))
    assert len(backups) == 1
    assert backups[0].stat().st_size > 0
