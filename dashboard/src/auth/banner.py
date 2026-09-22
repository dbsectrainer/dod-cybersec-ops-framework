"""
DoD Warning Banner Component

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import streamlit as st


def show_dod_banner():
    """Display the DoD warning banner and handle acknowledgment."""
    if "banner_acknowledged" not in st.session_state:
        st.session_state.banner_acknowledged = False

    if not st.session_state.banner_acknowledged:
        with st.container():
            st.markdown(
                """
            <style>
            .dod-banner {
                background-color: #002D62;
                color: white;
                padding: 20px;
                margin-bottom: 20px;
                text-align: left;
                font-family: monospace;
                border: 2px solid #FFD700;
                border-radius: 5px;
            }
            .dod-header {
                color: #FFD700;
                font-size: 1.2em;
                font-weight: bold;
                margin-bottom: 15px;
                text-align: center;
            }
            .dod-warning {
                color: #FF4B4B;
                font-weight: bold;
                margin: 10px 0;
            }
            </style>
            <div class='dod-banner'>
            <div class='dod-header'>U.S. DEPARTMENT OF DEFENSE WARNING STATEMENT</div>
            <div class='dod-warning'>!! ATTENTION !! This is a Department of Defense (DoD) Information System (IS)</div>

            You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.

            By using this IS (which includes any device attached to this IS), you consent to the following conditions:

            1. The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to:
               - Penetration testing
               - COMSEC monitoring
               - Network operations and defense
               - Personnel misconduct (PM)
               - Law enforcement (LE)
               - Counterintelligence (CI) investigations

            2. At any time, the USG may inspect and seize data stored on this IS.

            3. Communications using, or data stored on, this IS:
               - Are not private
               - Are subject to routine monitoring, interception, and search
               - May be disclosed or used for any USG-authorized purpose

            4. This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.

            5. Notwithstanding the above, using this IS does not constitute consent to:
               - PM, LE or CI investigative searching or monitoring of the content of privileged communications
               - Work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants
               - Such communications and work product are private and confidential

            For complete details, see the User Agreement.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            <style>
            .banner-controls {
                text-align: center;
                margin-top: 20px;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 215, 0, 0.3);
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            }
            .banner-controls .stButton > button {
                width: 100%;
                background-color: #FFD700;
                color: #002D62;
                font-weight: bold;
                border: none;
                padding: 10px 20px;
                margin-top: 10px;
            }
            .banner-controls .stButton > button:hover {
                background-color: #FFC000;
            }
            .banner-checkbox {
                color: #FFD700;
                font-weight: bold;
            }
            </style>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("<div class='banner-controls'>", unsafe_allow_html=True)
            st.markdown("<div class='banner-checkbox'>", unsafe_allow_html=True)
            st.checkbox("I have read and acknowledge the above warning", key="acknowledge_checkbox")
            st.markdown("</div>", unsafe_allow_html=True)
            if st.button("Acknowledge and Proceed", type="primary", use_container_width=True):
                if st.session_state.acknowledge_checkbox:
                    st.session_state.banner_acknowledged = True
                    st.rerun()
                else:
                    st.error("Please acknowledge the warning statement to proceed.")
            st.markdown("</div>", unsafe_allow_html=True)
            st.stop()
