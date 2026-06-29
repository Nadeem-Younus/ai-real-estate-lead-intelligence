from crewai import Agent
from backend.services.llm_service import llm

from backend.tools.brevo_tools import (
    GenerateFollowupEmailTool
)

followup_agent = Agent(
    role="Customer Relationship Manager",

    goal="""
    Generate personalized follow-up communication
    to maintain engagement with prospective buyers.
    """,

    backstory="""
    You are a real estate customer engagement
    specialist known for creating professional
    and persuasive communication.
    """,
    llm=llm,
    verbose=True
)