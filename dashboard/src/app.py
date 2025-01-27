"""
DoD Cybersecurity Operations Dashboard

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Security Headers
st.set_page_config(
    page_title="DoD Cybersecurity Operations Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Authentication
def check_password():
    """Returns `True` if the user had a correct password."""
    def password_entered():
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("Login", on_click=password_entered)
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.error("😕 User not known or password incorrect")
        st.button("Login", on_click=password_entered)
        return False
    else:
        # Password correct
        return True

if not check_password():
    st.stop()

# Classification Banner
st.markdown("""
    <div style='background-color: #f0f2f6; padding: 10px; text-align: center; font-weight: bold;'>
        UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
    </div>
    """, unsafe_allow_html=True)

# Title
st.title("DoD Cybersecurity Operations Dashboard")
st.markdown(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} EST*")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Security Operations", "Compliance Status", "System Health", 
     "Incident Response", "Asset Management", "Compliance Reports"]
)

# Mock Data Generation Functions
def generate_incident_data():
    dates = pd.date_range(start='2025-01-01', end='2025-01-27', freq='D')
    incidents = np.random.randint(1, 20, size=len(dates))
    return pd.DataFrame({'Date': dates, 'Incidents': incidents})

def generate_compliance_data():
    categories = ['STIG', 'RMF', 'Zero Trust', 'Cloud Security']
    compliance = np.random.uniform(70, 100, size=len(categories))
    return pd.DataFrame({'Category': categories, 'Compliance': compliance})

def generate_system_health():
    services = ['AWS', 'Azure', 'Platform One', 'milCloud 2.0']
    availability = np.random.uniform(98, 100, size=len(services))
    return pd.DataFrame({'Service': services, 'Availability': availability})

# Page Content
if page == "Security Operations":
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
        alert_counts = np.random.randint(10, 100, size=len(alert_types))
        fig = px.pie(values=alert_counts, names=alert_types,
                    title='Alert Severity Distribution')
        st.plotly_chart(fig, use_container_width=True)

elif page == "Compliance Status":
    # Compliance Metrics
    st.subheader("Compliance Status Overview")
    compliance_data = generate_compliance_data()
    fig = px.bar(compliance_data, x='Category', y='Compliance',
                 title='Compliance Scores by Category')
    st.plotly_chart(fig, use_container_width=True)
    
    # Control Implementation Status
    st.subheader("Control Implementation Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Implemented Controls", "342/400", "85.5%")
    with col2:
        st.metric("In Progress", "48/400", "12%")
    with col3:
        st.metric("Not Started", "10/400", "2.5%")

elif page == "System Health":
    # System Health Metrics
    st.subheader("System Availability")
    health_data = generate_system_health()
    fig = px.bar(health_data, x='Service', y='Availability',
                 title='Service Availability')
    st.plotly_chart(fig, use_container_width=True)
    
    # Resource Utilization
    st.subheader("Resource Utilization")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("CPU Usage", "45%", "-5%")
    with col2:
        st.metric("Memory Usage", "62%", "3%")
    with col3:
        st.metric("Storage Usage", "78%", "2%")

elif page == "Incident Response":
    # Active Incidents
    st.subheader("Active Incidents")
    
    # Mock incident data
    incidents = pd.DataFrame({
        'ID': ['INC-001', 'INC-002', 'INC-003'],
        'Severity': ['High', 'Medium', 'Critical'],
        'Status': ['In Progress', 'Under Investigation', 'Containment'],
        'Time': ['2h 15m', '45m', '4h 30m']
    })
    
    st.table(incidents)
    
    # Response Team Status
    st.subheader("Response Team Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Available Teams", "3/4", "-1")
    with col2:
        st.metric("Average Response Time", "15 min", "-2 min")
    with col3:
        st.metric("Open Tickets", "5", "+2")

elif page == "Asset Management":
    # Asset Overview
    st.subheader("Cloud Resource Distribution")
    
    # Mock asset data
    cloud_resources = {
        'AWS GovCloud': 150,
        'Azure Government': 120,
        'Platform One': 80,
        'milCloud 2.0': 50
    }
    
    fig = px.pie(values=list(cloud_resources.values()),
                 names=list(cloud_resources.keys()),
                 title='Cloud Resource Distribution')
    st.plotly_chart(fig, use_container_width=True)
    
    # Security Status
    st.subheader("Security Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Compliant Systems", "385/400", "96.25%")
    with col2:
        st.metric("Patch Status", "398/400", "99.5%")
    with col3:
        st.metric("Security Findings", "12", "-3")

else:  # Compliance Reports
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
        st.info("Generating report... Please wait.")
        # Mock report generation delay
        import time
        time.sleep(2)
        st.success("Report generated successfully!")
        st.download_button(
            label="Download Report",
            data="Mock report data",
            file_name=f"{report_type.lower().replace(' ', '_')}_{date_range[0]}.pdf"
        )

# Footer
st.markdown("""
    <div style='background-color: #f0f2f6; padding: 10px; text-align: center;'>
        <small>DoD Cybersecurity Operations Framework - For Official Use Only</small>
    </div>
    """, unsafe_allow_html=True)
