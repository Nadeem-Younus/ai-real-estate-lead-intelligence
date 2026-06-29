from crewai.tools import BaseTool

from backend.mcp.client import call_tool
from backend.services.config import settings


class GenerateFollowupEmailTool(BaseTool):

    name: str = "Generate Followup Email"

    description: str = (
        "Generate a professional follow-up email"
    )

    def _run(
        self,
        customer_name: str,
        property_name: str
    ):

        return call_tool(
            server_url=settings.BREVO_MCP_URL,
            endpoint="generate_followup_email",
            payload={
                "customer_name": customer_name,
                "property_name": property_name
            }
        )