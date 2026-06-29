from backend.mcp.client import call_tool
from backend.services.config import settings

result = call_tool(
    server_url=settings.BREVO_MCP_URL,
    endpoint="send_email",
    payload={
        "to_email": "nadeem.younus2007@gmail.com",
        "subject": "Test Email",
        "body": "Hello from AI Real Estate Lead Intelligence"
    }
)

print(result)