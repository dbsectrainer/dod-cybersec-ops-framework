"""
Session Management Module

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

from datetime import datetime, timedelta
import streamlit as st

from utils import load_config

# Security configuration, sourced from config.yaml so it can't drift from the
# values the rest of the app (and the UI copy in login.py) advertise.
try:
    _config = load_config()
    SESSION_TIMEOUT = _config["security"]["session_timeout"] // 60  # minutes
    MAX_LOGIN_ATTEMPTS = _config["security"]["max_login_attempts"]
except Exception:
    # Fall back to config.yaml's documented defaults if it can't be loaded
    # (e.g. running outside the normal src/ working directory).
    SESSION_TIMEOUT = 30  # minutes
    MAX_LOGIN_ATTEMPTS = 3
LOCKOUT_DURATION = 30  # minutes


def init_session_state():
    """Initialize session state variables."""
    if "login_attempts" not in st.session_state:
        st.session_state.login_attempts = 0
    if "last_activity" not in st.session_state:
        st.session_state.last_activity = datetime.now()
    if "last_login_time" not in st.session_state:
        st.session_state.last_login_time = None
    if "lockout_until" not in st.session_state:
        st.session_state.lockout_until = None
    if "security_events" not in st.session_state:
        st.session_state.security_events = []


def log_security_event(event_type, details):
    """Log security-related events."""
    event = {
        "timestamp": datetime.now(),
        "type": event_type,
        "details": details,
        "session_id": id(st.session_state),
    }
    if "security_events" not in st.session_state:
        st.session_state.security_events = []
    st.session_state.security_events.append(event)


def check_session_timeout():
    """Check if the current session has timed out."""
    if "password_correct" in st.session_state and st.session_state.password_correct:
        time_inactive = datetime.now() - st.session_state.last_activity
        if time_inactive.total_seconds() > SESSION_TIMEOUT * 60:
            st.session_state.password_correct = False
            st.session_state.last_activity = datetime.now()
            log_security_event("session_timeout", "Session expired due to inactivity")
            st.warning("Your session has expired due to inactivity. Please log in again.")
            st.rerun()
        else:
            st.session_state.last_activity = datetime.now()


def check_account_lockout():
    """Check if the account is currently locked out."""
    if st.session_state.lockout_until and datetime.now() < st.session_state.lockout_until:
        remaining_time = (st.session_state.lockout_until - datetime.now()).seconds // 60
        st.error(f"Account is locked. Please try again in {remaining_time} minutes.")
        log_security_event(
            "lockout_check",
            f"Attempted access during lockout period. {remaining_time} minutes remaining",
        )
        return True
    elif st.session_state.lockout_until and datetime.now() >= st.session_state.lockout_until:
        st.session_state.lockout_until = None
        st.session_state.login_attempts = 0
        log_security_event("lockout_expired", "Account lockout period expired")
    return False


def handle_failed_login():
    """Handle failed login attempts and implement lockout if necessary."""
    st.session_state.login_attempts += 1
    remaining_attempts = MAX_LOGIN_ATTEMPTS - st.session_state.login_attempts

    if remaining_attempts <= 0:
        st.session_state.lockout_until = datetime.now() + timedelta(minutes=LOCKOUT_DURATION)
        log_security_event(
            "account_locked",
            f"Account locked for {LOCKOUT_DURATION} minutes due to multiple failed attempts",
        )
        st.error(f"Maximum login attempts exceeded. Account locked for {LOCKOUT_DURATION} minutes.")
        st.stop()
    else:
        log_security_event(
            "failed_login", f"Failed login attempt. {remaining_attempts} attempts remaining"
        )
        st.error(f"Invalid credentials. {remaining_attempts} attempts remaining.")


def handle_successful_login(username):
    """Handle successful login procedures."""
    st.session_state.password_correct = True
    st.session_state.last_login_time = datetime.now()
    st.session_state.login_attempts = 0
    st.session_state.lockout_until = None
    log_security_event("successful_login", f"User {username} logged in successfully")
    if "password" in st.session_state:
        del st.session_state["password"]  # Clear password from session state


def show_system_status():
    """Display system status information in the sidebar."""
    st.sidebar.markdown(
        """
    <div style='background-color: #1a1a1a; padding: 10px; border-radius: 5px;'>
        <h4 style='color: #00ff00; margin: 0;'>System Status</h4>
        <p style='color: #ffffff; margin: 5px 0;'>🟢 System Operational</p>
        <p style='color: #ffffff; margin: 5px 0;'>Classification: FOUO</p>
        <p style='color: #ffffff; margin: 5px 0;'>Session Timeout: {} min</p>
        <p style='color: #ffffff; margin: 5px 0;'>Last Activity: {}</p>
    </div>
    """.format(SESSION_TIMEOUT, st.session_state.last_activity.strftime("%Y-%m-%d %H:%M:%S")),
        unsafe_allow_html=True,
    )


def get_session_info():
    """Return current session information."""
    return {
        "session_id": id(st.session_state),
        "login_time": st.session_state.last_login_time,
        "last_activity": st.session_state.last_activity,
        "remaining_time": SESSION_TIMEOUT
        - ((datetime.now() - st.session_state.last_activity).seconds // 60)
        if "last_activity" in st.session_state
        else SESSION_TIMEOUT,
    }
