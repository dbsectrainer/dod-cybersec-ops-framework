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
    log_security_event
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
    generate_mock_report,
    format_classification_banner,
    format_footer,
    format_metric_container,
    format_alert,
    format_table
)

# Security Headers
st.set_page_config(
    page_title="DoD Cybersecurity Operations Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
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
    log_security_event('logout', 'User logged out')
    st.session_state["password_correct"] = False
    st.rerun()

page = st.sidebar.radio(
    "Select Page",
    ["Security Operations", "Compliance Status", "System Health", 
     "Incident Response", "Asset Management", "Compliance Reports"]
)

# Page Content
if page == "Security Operations":
    log_security_event('page_view', 'Accessed Security Operations page')
    # Security Operations Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Incident Trends")
        incident_data = generate_incident_data()
        fig = px.line(incident_data, x='Date', y='Incidents',
                     title='Daily Security Incidents')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Alert Distribution")
        alert_types = ['Critical', 'High', 'Medium', 'Low']
        alert_counts = [25, 45, 70, 30]  # More realistic distribution
        fig = px.pie(values=alert_counts, names=alert_types,
                    title='Alert Severity Distribution')
        st.plotly_chart(fig, use_container_width=True)

elif page == "Compliance Status":
    log_security_event('page_view', 'Accessed Compliance Status page')
    # Compliance Metrics
    st.subheader("Compliance Status Overview")
    compliance_data = generate_compliance_data()
    fig = px.bar(compliance_data, x='Category', y='Compliance',
                 title='Compliance Scores by Category')
    st.plotly_chart(fig, use_container_width=True)
    
    # Control Implementation Status
    st.subheader("Control Implementation Status")
    control_status = get_control_status()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Implemented Controls", 
                 control_status['implemented']['value'],
                 control_status['implemented']['percentage'])
    with col2:
        st.metric("In Progress", 
                 control_status['in_progress']['value'],
                 control_status['in_progress']['percentage'])
    with col3:
        st.metric("Not Started", 
                 control_status['not_started']['value'],
                 control_status['not_started']['percentage'])

elif page == "System Health":
    log_security_event('page_view', 'Accessed System Health page')
    # System Health Metrics
    st.subheader("System Availability")
    health_data = generate_system_health()
    fig = px.bar(health_data, x='Service', y='Availability',
                 title='Service Availability')
    st.plotly_chart(fig, use_container_width=True)
    
    # Resource Utilization
    st.subheader("Resource Utilization")
    resource_metrics = get_resource_metrics()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("CPU Usage", 
                 resource_metrics['cpu']['value'],
                 resource_metrics['cpu']['delta'])
    with col2:
        st.metric("Memory Usage", 
                 resource_metrics['memory']['value'],
                 resource_metrics['memory']['delta'])
    with col3:
        st.metric("Storage Usage", 
                 resource_metrics['storage']['value'],
                 resource_metrics['storage']['delta'])

elif page == "Incident Response":
    log_security_event('page_view', 'Accessed Incident Response page')
    # Active Incidents
    st.subheader("Active Incidents")
    incidents = get_mock_incidents()
    
    # Apply styling based on severity
    def highlight_severity(row):
        color_map = {
            'Critical': 'background-color: rgba(220, 53, 69, 0.3)',    # Red with opacity
            'High': 'background-color: rgba(255, 193, 7, 0.3)',        # Yellow with opacity
            'Medium': 'background-color: rgba(13, 110, 253, 0.3)'      # Blue with opacity
        }
        return [color_map.get(row['Severity'], '')] * len(row)
    
    # Apply the styling to the dataframe
    styled_incidents = incidents.style.apply(highlight_severity, axis=1)
    
    # Display using native Streamlit component
    st.dataframe(styled_incidents, use_container_width=True)
    
    # Response Team Status
    st.subheader("Response Team Status")
    team_metrics = get_team_metrics()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Available Teams", 
                 team_metrics['available_teams']['value'],
                 team_metrics['available_teams']['delta'])
    with col2:
        st.metric("Average Response Time", 
                 team_metrics['response_time']['value'],
                 team_metrics['response_time']['delta'])
    with col3:
        st.metric("Open Tickets", 
                 team_metrics['open_tickets']['value'],
                 team_metrics['open_tickets']['delta'])

elif page == "Asset Management":
    log_security_event('page_view', 'Accessed Asset Management page')
    # Asset Overview
    st.subheader("Cloud Resource Distribution")
    cloud_resources = get_cloud_resources()
    fig = px.pie(values=list(cloud_resources.values()),
                 names=list(cloud_resources.keys()),
                 title='Cloud Resource Distribution')
    st.plotly_chart(fig, use_container_width=True)
    
    # Security Status
    st.subheader("Security Status")
    security_metrics = get_security_metrics()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Compliant Systems", 
                 security_metrics['compliant_systems']['value'],
                 security_metrics['compliant_systems']['percentage'])
    with col2:
        st.metric("Patch Status", 
                 security_metrics['patch_status']['value'],
                 security_metrics['patch_status']['percentage'])
    with col3:
        st.metric("Security Findings", 
                 security_metrics['security_findings']['value'],
                 security_metrics['security_findings']['delta'])

else:  # Compliance Reports
    log_security_event('page_view', 'Accessed Compliance Reports page')
    # Compliance Reports
    st.subheader("Compliance Report Generation")
    
    report_type = st.selectbox(
        "Select Report Type",
        ["STIG Compliance", "RMF Status", "Audit Logs", "Control Validation"]
    )
    
    date_range = st.date_input(
        "Select Date Range",
        value=(datetime.now() - timedelta(days=30), datetime.now())
    )
    
    if st.button("Generate Report"):
        st.markdown(format_alert("Generating report... Please wait.", "info"), 
                   unsafe_allow_html=True)
        # Mock report generation delay
        import time
        time.sleep(2)
        
        report_data = generate_mock_report(
            report_type, 
            date_range[0].strftime('%Y-%m-%d'),
            date_range[1].strftime('%Y-%m-%d')
        )
        
        st.markdown(format_alert("Report generated successfully!", "success"), 
                   unsafe_allow_html=True)
        st.download_button(
            label="Download Report",
            data=report_data,
            file_name=f"{report_type.lower().replace(' ', '_')}_{date_range[0]}.pdf"
        )

# Footer
st.markdown(format_footer(), unsafe_allow_html=True)
