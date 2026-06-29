from crewai import Agent
from backend.services.llm_service import llm


lead_agent = Agent(
    role="Lead Qualification Specialist",

    goal="""
    Evaluate incoming real estate leads and
    determine their buying intent, urgency,
    and sales priority.
    """,

    backstory="""
    You are an experienced real estate sales analyst.
    Your job is to evaluate prospective buyers,
    identify serious opportunities, and help sales
    teams focus on the highest-value leads.
    """,
    llm=llm,
    memory=True,
    allow_delegation=True,
    verbose=True
)