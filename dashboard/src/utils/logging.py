"""
Logging utilities for the DoD Cybersecurity Operations Dashboard

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import logging
import logging.handlers
import syslog
from pathlib import Path
import shutil
from datetime import datetime
from typing import Dict


class LogHandler:
    """Custom log handler with syslog integration and backup capabilities."""

    def __init__(self, config: Dict):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging handlers based on configuration."""
        # File handler with rotation
        log_dir = Path(self.config["logging"]["handlers"]["file"]["filename"]).parent
        log_dir.mkdir(parents=True, exist_ok=True)

        file_handler = logging.handlers.RotatingFileHandler(
            filename=self.config["logging"]["handlers"]["file"]["filename"],
            maxBytes=self.config["logging"]["handlers"]["file"]["max_size"],
            backupCount=self.config["logging"]["handlers"]["file"]["backup_count"],
        )
        file_handler.setFormatter(logging.Formatter(self.config["logging"]["format"]))
        self.logger.addHandler(file_handler)

        # Syslog handler
        if self.config["logging"]["handlers"]["syslog"]["enabled"]:
            syslog_handler = logging.handlers.SysLogHandler(
                address="/dev/log",
                facility=getattr(
                    syslog,
                    f"LOG_{self.config['logging']['handlers']['syslog']['facility'].upper()}",
                ),
            )
            syslog_handler.setFormatter(logging.Formatter(self.config["logging"]["format"]))
            self.logger.addHandler(syslog_handler)

    def backup_logs(self):
        """Create backup of log files."""
        try:
            log_file = self.config["logging"]["handlers"]["file"]["filename"]
            backup_dir = Path(log_file).parent / "backups"
            backup_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = backup_dir / f"dashboard_logs_{timestamp}.log"

            shutil.copy2(log_file, backup_file)
            self.logger.info(f"Created log backup: {backup_file}")
        except Exception as e:
            self.logger.error(f"Failed to backup logs: {str(e)}")
            raise
