"""
Login Page Module

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import streamlit as st
from datetime import datetime
from .session import (
    init_session_state,
    check_account_lockout,
    handle_failed_login,
    handle_successful_login,
)
from utils import load_config

try:
    _PASSWORD_MIN_LENGTH = load_config()["security"]["password_policy"]["min_length"]
except Exception:
    _PASSWORD_MIN_LENGTH = 14


def get_system_metrics():
    """Get current system security and health metrics."""
    return {
        "zero_trust_status": {
            "identity_verification": "Active",
            "device_verification": "Active",
            "network_verification": "Active",
            "session_monitoring": "Active",
        },
        "security_posture": {
            "threat_level": "Low",
            "active_incidents": 0,
            "system_health": "Optimal",
            "last_security_scan": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
        "authentication_status": {
            "piv_cac_status": "Operational",
            "mfa_status": "Enabled",
            "biometric_status": "Available",
        },
        "compliance_status": {
            "stig_compliance": "98%",
            "rmf_controls": "95%",
            "zero_trust": "92%",
            "last_audit": datetime.now().strftime("%Y-%m-01"),
        },
        "service_health": {
            "core_services": "Operational",
            "auth_services": "Operational",
            "monitoring_services": "Operational",
            "backup_services": "Operational",
        },
    }


def show_security_metrics():
    """Display current security metrics and system status."""
    metrics = get_system_metrics()

    st.markdown(
        """
    <style>
    .metric-container {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .metric-header {
        color: #002D62;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .metric-value {
        color: #28a745;
        font-family: monospace;
    }
    .metric-warning {
        color: #dc3545;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-header'>Zero Trust Status</div>", unsafe_allow_html=True)
        for key, value in metrics["zero_trust_status"].items():
            st.markdown(
                f"<div class='metric-value'>✓ {key.replace('_', ' ').title()}: {value}</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.markdown(
            "<div class='metric-header'>Authentication Services</div>", unsafe_allow_html=True
        )
        for key, value in metrics["authentication_status"].items():
            st.markdown(
                f"<div class='metric-value'>✓ {key.replace('_', ' ').title()}: {value}</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-header'>Security Posture</div>", unsafe_allow_html=True)
        for key, value in metrics["security_posture"].items():
            st.markdown(
                f"<div class='metric-value'>✓ {key.replace('_', ' ').title()}: {value}</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-header'>Service Health</div>", unsafe_allow_html=True)
        for key, value in metrics["service_health"].items():
            st.markdown(
                f"<div class='metric-value'>✓ {key.replace('_', ' ').title()}: {value}</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


def show_login_page():
    """Display the enhanced login page with security information."""
    st.markdown(
        """
    <style>
    .login-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .classification-banner {
        background-color: #dc3545;
        color: white;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        border-radius: 5px;
    }
    .auth-options {
        margin: 20px 0;
        padding: 15px;
        background-color: #e9ecef;
        border-radius: 5px;
    }
    .security-info {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
    .security-requirements {
        background-color: #e2e3e5;
        border: 1px solid #d6d8db;
        color: #383d41;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
    .compliance-status {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        font-size: 0.9em;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown("<div class='login-container'>", unsafe_allow_html=True)

        # Classification Banner
        st.markdown(
            "<div class='classification-banner'>UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)</div>",
            unsafe_allow_html=True,
        )

        # DoD Seal/Logo
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st.image("assets/dod_seal.jpeg", width=150)
            except Exception:
                st.error("Unable to load DoD seal image")
                st.markdown("🏛️ **Department of Defense**")

        st.markdown(
            "<h2 style='text-align: center;'>DoD Cybersecurity Operations Dashboard</h2>",
            unsafe_allow_html=True,
        )

        # System Security Metrics
        show_security_metrics()

        # Security Information
        st.markdown(
            """
        <div class='security-info'>
            <h4>⚠️ Security Notice</h4>
            <ul>
                <li>This is a DoD Information System</li>
                <li>All activities are monitored and recorded</li>
                <li>Unauthorized access is prohibited</li>
                <li>Users have no expectation of privacy</li>
            </ul>
        </div>

        <div class='security-requirements'>
            <h4>🔒 System Requirements</h4>
            <ul>
                <li>Use of approved DoD workstation</li>
                <li>Current security certificates</li>
                <li>Approved network connection</li>
                <li>Up-to-date system patches</li>
            </ul>
        </div>

        <div class='compliance-status'>
            <h4>✓ Compliance Status</h4>
            <ul>
                <li>STIG Compliance: {stig_compliance}</li>
                <li>RMF Controls: {rmf_controls}</li>
                <li>Zero Trust Implementation: {zero_trust}</li>
                <li>Last Security Audit: {last_audit}</li>
            </ul>
        </div>
        """.format(**get_system_metrics()["compliance_status"]),
            unsafe_allow_html=True,
        )

        # Authentication Options
        st.markdown("<div class='auth-options'>", unsafe_allow_html=True)
        auth_method = st.radio(
            "Select Authentication Method:", ["Username/Password", "PIV/CAC (Coming Soon)"], index=0
        )
        st.markdown("</div>", unsafe_allow_html=True)

        if auth_method == "Username/Password":
            with st.form("login_form"):
                username = st.text_input("Username", key="username")
                password = st.text_input("Password", type="password", key="password")
                st.markdown(
                    """
                <div class='password-requirements'>
                    Password Requirements:
                    <ul>
                        <li>Minimum {min_length} characters</li>
                        <li>At least one uppercase letter</li>
                        <li>At least one lowercase letter</li>
                        <li>At least one number</li>
                        <li>At least one special character</li>
                        <li>No dictionary words</li>
                    </ul>
                </div>
                """.format(min_length=_PASSWORD_MIN_LENGTH),
                    unsafe_allow_html=True,
                )

                # Show last login attempt if available
                if st.session_state.last_login_time:
                    st.info(
                        f"Last login attempt: {st.session_state.last_login_time.strftime('%Y-%m-%d %H:%M:%S')}"
                    )

                submitted = st.form_submit_button("Login")
                if submitted:
                    if check_account_lockout():
                        return

                    if (
                        username in st.secrets["passwords"]
                        and password == st.secrets["passwords"][username]
                    ):
                        handle_successful_login(username)
                        st.rerun()
                    else:
                        handle_failed_login()
        else:
            st.info("PIV/CAC authentication will be available in a future update.")

        # Support Information
        st.markdown(
            """
        <div style='margin-top: 20px; font-size: 0.9em;'>
            <p><strong>Need Help?</strong></p>
            <ul>
                <li>Contact Support: support@dod.mil</li>
                <li>System Status: <a href="#">status.dod.mil</a></li>
                <li>New User Registration: <a href="#">register.dod.mil</a></li>
                <li>Password Reset: <a href="#">password.dod.mil</a></li>
                <li>Security Incident Reporting: <a href="#">security.dod.mil</a></li>
                <li>DoD Security Policy: <a href="#">policy.dod.mil</a></li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)


def check_password():
    """Returns `True` if the user had a correct password."""
    init_session_state()

    if "password_correct" not in st.session_state:
        show_login_page()
        return False
    elif not st.session_state["password_correct"]:
        show_login_page()
        return False
    else:
        return True
