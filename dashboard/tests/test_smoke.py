"""
Smoke tests for the DoD Cybersecurity Operations Dashboard.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)

These exercise import wiring and config loading rather than UI behavior
(there's no Streamlit test harness here) — enough to catch the kind of
regressions this modernization pass fixed: a broken import, or session/
login code silently drifting from config.yaml again.
"""

from pathlib import Path

DASHBOARD_DIR = Path(__file__).resolve().parent.parent
CONFIG_EXAMPLE = DASHBOARD_DIR / "config" / "config.yaml.example"


def test_utils_package_imports():
    import utils

    assert callable(utils.load_config)


def test_auth_package_imports():
    import auth

    assert callable(auth.check_password)


def test_load_config_from_example():
    from utils import load_config

    config = load_config(str(CONFIG_EXAMPLE))
    assert config["security"]["session_timeout"] == 1800
    assert config["security"]["password_policy"]["min_length"] == 14


def test_session_timeout_matches_config(monkeypatch):
    """Regression test: session.py must read its timeout from config.yaml
    (loaded relative to dashboard/src, its real runtime working directory)
    rather than a hardcoded constant that can silently drift from it."""
    import importlib

    import yaml

    real_config = yaml.safe_load((DASHBOARD_DIR / "config" / "config.yaml").read_text())

    monkeypatch.chdir(DASHBOARD_DIR / "src")
    session = importlib.import_module("auth.session")
    session = importlib.reload(session)

    assert session.SESSION_TIMEOUT == real_config["security"]["session_timeout"] // 60
    assert session.MAX_LOGIN_ATTEMPTS == real_config["security"]["max_login_attempts"]
