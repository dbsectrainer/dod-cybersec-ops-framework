"""
Unit tests for authentication session configuration.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

from auth.session import LOCKOUT_DURATION, MAX_LOGIN_ATTEMPTS, SESSION_TIMEOUT


def test_session_security_constants():
    assert SESSION_TIMEOUT == 15
    assert MAX_LOGIN_ATTEMPTS == 3
    assert LOCKOUT_DURATION == 30


def test_lockout_exceeds_session_timeout():
    assert LOCKOUT_DURATION >= SESSION_TIMEOUT
