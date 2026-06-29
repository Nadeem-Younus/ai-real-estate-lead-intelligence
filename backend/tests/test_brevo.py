from backend.services.config import settings
from backend.mcp.client import call_tool

print("BREVO_MCP_URL =", settings.BREVO_MCP_URL)

result = call_tool(
    server_url=settings.BREVO_MCP_URL,
    endpoint="generate_followup_email",
    payload={
        "customer_name": "John Smith",
        "property_name": "Luxury Villa Islamabad"
    }
)

print(result)