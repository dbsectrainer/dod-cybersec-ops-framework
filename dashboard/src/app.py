"""
DoD Cybersecurity Operations Dashboard

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta

from auth import (
    show_dod_banner,
    check_password,
    check_session_timeout,
    show_system_status,
    log_security_event,
)

from utils import (
    generate_incident_data,
    generate_compliance_data,
    generate_system_health,
    get_mock_incidents,
    get_cloud_resources,
    get_control_status,
    get_resource_metrics,
    get_team_metrics,
    get_security_metrics,
    format_classification_banner,
    format_footer,
    format_alert,
    LogHandler,
    ComplianceChecker,
    ReportGenerator,
    load_config,
    ComplianceStatus,
)

# Security Headers
st.set_page_config(
    page_title="DoD Cybersecurity Operations Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Show DoD banner before login
show_dod_banner()

# Check authentication
if not check_password():
    st.stop()

# Check session timeout
check_session_timeout()

# Classification Banner
st.markdown(format_classification_banner(), unsafe_allow_html=True)

# Title
st.title("DoD Cybersecurity Operations Dashboard")
st.markdown(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} EST*")

# Show system status in sidebar
show_system_status()

# Sidebar Navigation
st.sidebar.title("Navigation")

# Add logout button
if st.sidebar.button("Logout"):
    log_security_event("logout", "User logged out")
    st.session_state["password_correct"] = False
    st.rerun()

# Initialize handlers
config = load_config()
log_handler = LogHandler(config)
compliance_checker = ComplianceChecker(config)
report_generator = ReportGenerator(config)

page = st.sidebar.radio(
    "Select Page",
    [
        "Security Operations",
        "Compliance Status",
        "System Health",
        "Incident Response",
        "Asset Management",
        "Compliance Reports",
        "System Logs",
    ],
)

# Page Content
if page == "Security Operations":
    log_security_event("page_view", "Accessed Security Operations page")
    # Security Operations Metrics
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Incident Trends")
        incident_data = generate_incident_data()
        fig = px.line(incident_data, x="Date", y="Incidents", title="Daily Security Incidents")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Alert Distribution")
        alert_types = ["Critical", "High", "Medium", "Low"]
        alert_counts = [25, 45, 70, 30]  # More realistic distribution
        fig = px.pie(values=alert_counts, names=alert_types, title="Alert Severity Distribution")
        st.plotly_chart(fig, use_container_width=True)

elif page == "Compliance Status":
    log_security_event("page_view", "Accessed Compliance Status page")
    # Compliance Metrics
    st.subheader("Compliance Status Overview")
    compliance_data = generate_compliance_data()
    fig = px.bar(
        compliance_data, x="Category", y="Compliance", title="Compliance Scores by Category"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Control Implementation Status
    st.subheader("Control Implementation Status")
    control_status = get_control_status()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Implemented Controls",
            control_status["implemented"]["value"],
            control_status["implemented"]["percentage"],
        )
    with col2:
        st.metric(
            "In Progress",
            control_status["in_progress"]["value"],
            control_status["in_progress"]["percentage"],
        )
    with col3:
        st.metric(
            "Not Started",
            control_status["not_started"]["value"],
            control_status["not_started"]["percentage"],
        )

elif page == "System Health":
    log_security_event("page_view", "Accessed System Health page")
    # System Health Metrics
    st.subheader("System Availability")
    health_data = generate_system_health()
    fig = px.bar(health_data, x="Service", y="Availability", title="Service Availability")
    st.plotly_chart(fig, use_container_width=True)

    # Resource Utilization
    st.subheader("Resource Utilization")
    resource_metrics = get_resource_metrics()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("CPU Usage", resource_metrics["cpu"]["value"], resource_metrics["cpu"]["delta"])
    with col2:
        st.metric(
            "Memory Usage", resource_metrics["memory"]["value"], resource_metrics["memory"]["delta"]
        )
    with col3:
        st.metric(
            "Storage Usage",
            resource_metrics["storage"]["value"],
            resource_metrics["storage"]["delta"],
        )

elif page == "Incident Response":
    log_security_event("page_view", "Accessed Incident Response page")
    # Active Incidents
    st.subheader("Active Incidents")
    incidents = get_mock_incidents()

    # Apply styling based on severity
    def highlight_severity(row):
        color_map = {
            "Critical": "background-color: rgba(220, 53, 69, 0.3)",  # Red with opacity
            "High": "background-color: rgba(255, 193, 7, 0.3)",  # Yellow with opacity
            "Medium": "background-color: rgba(13, 110, 253, 0.3)",  # Blue with opacity
        }
        return [color_map.get(row["Severity"], "")] * len(row)

    # Apply the styling to the dataframe
    styled_incidents = incidents.style.apply(highlight_severity, axis=1)

    # Display using native Streamlit component
    st.dataframe(styled_incidents, use_container_width=True)

    # Response Team Status
    st.subheader("Response Team Status")
    team_metrics = get_team_metrics()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Available Teams",
            team_metrics["available_teams"]["value"],
            team_metrics["available_teams"]["delta"],
        )
    with col2:
        st.metric(
            "Average Response Time",
            team_metrics["response_time"]["value"],
            team_metrics["response_time"]["delta"],
        )
    with col3:
        st.metric(
            "Open Tickets",
            team_metrics["open_tickets"]["value"],
            team_metrics["open_tickets"]["delta"],
        )

elif page == "Asset Management":
    log_security_event("page_view", "Accessed Asset Management page")
    # Asset Overview
    st.subheader("Cloud Resource Distribution")
    cloud_resources = get_cloud_resources()
    fig = px.pie(
        values=list(cloud_resources.values()),
        names=list(cloud_resources.keys()),
        title="Cloud Resource Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)

    # Security Status
    st.subheader("Security Status")
    security_metrics = get_security_metrics()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Compliant Systems",
            security_metrics["compliant_systems"]["value"],
            security_metrics["compliant_systems"]["percentage"],
        )
    with col2:
        st.metric(
            "Patch Status",
            security_metrics["patch_status"]["value"],
            security_metrics["patch_status"]["percentage"],
        )
    with col3:
        st.metric(
            "Security Findings",
            security_metrics["security_findings"]["value"],
            security_metrics["security_findings"]["delta"],
        )

elif page == "System Logs":
    log_security_event("page_view", "Accessed System Logs page")
    st.subheader("System Logs")

    # Log level filter
    log_level = st.selectbox("Log Level", ["ALL", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    # Date range filter. st.date_input can return a single date (while the
    # user is still picking the range end) instead of the expected 2-tuple,
    # so fall back to the default range until both dates are chosen.
    _default_log_range = (datetime.now() - timedelta(days=7), datetime.now())
    log_date_range = st.date_input("Date Range", value=_default_log_range)
    if not isinstance(log_date_range, tuple) or len(log_date_range) != 2:
        log_date_range = (_default_log_range[0].date(), _default_log_range[1].date())

    # Add log backup button
    if st.button("Backup Logs"):
        try:
            log_handler.backup_logs()
            st.markdown(
                format_alert("Logs backed up successfully!", "success"), unsafe_allow_html=True
            )
        except Exception as e:
            st.markdown(
                format_alert(f"Error backing up logs: {str(e)}", "error"), unsafe_allow_html=True
            )

    # Display logs
    try:
        with open(config["logging"]["handlers"]["file"]["filename"], "r") as f:
            logs = f.readlines()

        # Filter logs based on selected level and date range
        filtered_logs = []
        for log in logs:
            if log_level != "ALL" and log_level not in log:
                continue

            try:
                log_date = datetime.strptime(log.split(" - ")[0], "%Y-%m-%d %H:%M:%S,%f")
                if log_date.date() >= log_date_range[0] and log_date.date() <= log_date_range[1]:
                    filtered_logs.append(log)
            except ValueError:
                continue

        st.text_area("Log Output", "\n".join(filtered_logs), height=400)
    except Exception as e:
        st.markdown(format_alert(f"Error reading logs: {str(e)}", "error"), unsafe_allow_html=True)

else:  # Compliance Reports
    log_security_event("page_view", "Accessed Compliance Reports page")
    st.subheader("Compliance Report Generation")

    # Framework selection
    framework = st.selectbox("Select Framework", ["NIST RMF", "DISA STIG"])

    report_type = st.selectbox(
        "Report Type",
        ["Full Assessment", "Control Status", "Non-Compliant Items", "Executive Summary"],
    )

    report_format = st.selectbox("Report Format", ["PDF", "HTML", "CSV"])

    # See the log date-range filter above for why this guard is needed:
    # st.date_input can return a single date instead of a 2-tuple.
    _default_report_range = (datetime.now() - timedelta(days=30), datetime.now())
    date_range = st.date_input("Date Range", value=_default_report_range)
    if not isinstance(date_range, tuple) or len(date_range) != 2:
        date_range = (_default_report_range[0].date(), _default_report_range[1].date())

    if st.button("Generate Report"):
        try:
            st.markdown(
                format_alert("Running compliance checks... Please wait.", "info"),
                unsafe_allow_html=True,
            )

            # Run compliance checks
            compliance_results = compliance_checker.check_compliance(framework)

            # Generate statistics
            total = len(compliance_results)
            compliant = sum(1 for r in compliance_results if r.status == ComplianceStatus.COMPLIANT)
            non_compliant = sum(
                1 for r in compliance_results if r.status == ComplianceStatus.NON_COMPLIANT
            )
            partial = sum(1 for r in compliance_results if r.status == ComplianceStatus.PARTIAL)

            # Display summary
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Controls", total)
            col2.metric("Compliant", compliant)
            col3.metric("Non-Compliant", non_compliant)
            col4.metric("Partial", partial)

            # Generate report
            report_data = report_generator.generate_report(
                report_type,
                {
                    "framework": framework,
                    "results": compliance_results,
                    "statistics": {
                        "total": total,
                        "compliant": compliant,
                        "non_compliant": non_compliant,
                        "partial": partial,
                    },
                    "date_range": date_range,
                },
                format=report_format.lower(),
            )

            st.markdown(
                format_alert("Report generated successfully!", "success"), unsafe_allow_html=True
            )

            st.download_button(
                label="Download Report",
                data=report_data,
                file_name=f"{framework.lower().replace(' ', '_')}_{report_type.lower().replace(' ', '_')}_{date_range[0]}.{report_format.lower()}",
            )

        except Exception as e:
            st.markdown(
                format_alert(f"Error generating report: {str(e)}", "error"), unsafe_allow_html=True
            )

# Footer
st.markdown(format_footer(), unsafe_allow_html=True)
