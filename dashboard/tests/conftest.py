"""
Pytest configuration: make the dashboard/src packages importable.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
