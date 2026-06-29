import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from backend.crews.real_estate_crew import RealEstateCrew
from backend.mcp.client import call_tool
from backend.services.config import settings

st.set_page_config(
    page_title="AI Real Estate Lead Intelligence",
    page_icon="🏠",
    layout="wide"
)

st.title(
    "🏠 AI Real Estate Lead Intelligence"
)

st.caption(
    "CrewAI + MCP + Google Places + Brevo"
)

st.markdown(
    """
    Multi-Agent Real Estate Intelligence Platform

    Powered by:
    - CrewAI
    - MCP Tools
    - OpenAI
    - Google Places API
    - Brevo
    """
)

# --------------------------------------------------
# LEAD FORM
# --------------------------------------------------

with st.form("lead_form"):

    col1, col2 = st.columns(2)

    with col1:

        customer_name = st.text_input(
            "Customer Name"
        )

        budget = st.number_input(
            "Budget (PKR)",
            min_value=1000000,
            value=30000000,
            step=1000000
        )

    with col2:

        property_type = st.selectbox(
            "Property Type",
            [
                "House",
                "Apartment",
                "Villa",
                "Shop",
                "Office"
            ]
        )

        timeline = st.selectbox(
            "Timeline",
            [
                "Immediate",
                "30 days",
                "90 days",
                "6 months"
            ]
        )

    location = st.text_input(
        "Location",
        value="Islamabad"
    )

    submitted = st.form_submit_button(
        "Analyze Lead"
    )

# --------------------------------------------------
# RUN CREW
# --------------------------------------------------

if submitted:

    with st.spinner(
        "Running AI Agents..."
    ):

        crew = RealEstateCrew()

        result = crew.run(
            customer_name=customer_name,
            budget=budget,
            property_type=property_type,
            timeline=timeline,
            location=location
        )

        st.session_state["analysis_result"] = result

# --------------------------------------------------
# SHOW RESULTS
# --------------------------------------------------

if "analysis_result" in st.session_state:

    result = st.session_state["analysis_result"]

    st.success(
        "Analysis Complete"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Lead Analysis",
            "Nearby Properties",
            "Neighborhood Intelligence",
            "Follow-up Email"
        ]
    )

    # ------------------------------------------
    # TAB 1
    # ------------------------------------------

    with tab1:

        st.markdown(result["lead_analysis"])

    # ------------------------------------------
    # TAB 2
    # ------------------------------------------

    with tab2:

        st.markdown(result["property_recommendations"])

    # ------------------------------------------
    # TAB 3
    # ------------------------------------------

    with tab3:

        st.markdown(result["neighborhood_intelligence"])

    # ------------------------------------------
    # TAB 4
    # ------------------------------------------

    with tab4:

        st.subheader("Review Before Sending")

        edited_email = st.text_area(
            "Edit Email",
            value=result["followup_email"],
            height=350,
            key="edited_email"
        )

        recipient_email = st.text_input(
            "Recipient Email",
            key="recipient_email"
        )

        if st.button(
            "📧 Send Email"
        ):

            if not recipient_email:

                st.warning(
                    "Please enter recipient email."
                )

            else:

                response = call_tool(
                    server_url=settings.BREVO_MCP_URL,
                    endpoint="send_email",
                    payload={
                        "to_email": recipient_email,
                        "subject": "Property Follow-Up",
                        "body": edited_email
                    }
                )

                if "messageId" in str(response):
                    
                    st.success(
                        "✅ Email sent successfully."
                    )

                else:
                    st.error(
                        "❌ Email sending failed."
                    )