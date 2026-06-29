from crewai import Agent

from backend.services.llm_service import llm

from backend.tools.neighborhood_tools import (
    NeighborhoodIntelligenceTool
)

market_agent = Agent(
    role="Neighborhood Intelligence Specialist",

    goal="""
    Analyze neighborhoods around properties
    and provide useful location insights
    for potential buyers.
    """,

    backstory="""
    You are a real estate location expert.
    You evaluate education, healthcare,
    recreation, shopping and transportation
    facilities around a property.
    """,

    llm=llm,

    tools=[
        NeighborhoodIntelligenceTool()
    ],

    verbose=True
)