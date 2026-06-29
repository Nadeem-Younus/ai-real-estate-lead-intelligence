from crewai import Agent
from backend.services.llm_service import llm

from backend.tools.property_tools import (
    PropertySearchTool
)

property_agent = Agent(
    role="Property Matching Consultant",

    goal="""
    Match customer requirements with available
    properties and identify the most suitable options.
    """,

    backstory="""
    You are a senior real estate consultant
    specializing in matching buyers with properties
    that fit their budget and preferences.
    """,
    
    llm=llm,

    tools=[
        PropertySearchTool()
    ],

    verbose=True
)