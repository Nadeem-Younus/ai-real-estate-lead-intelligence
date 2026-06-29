import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

sys.path.append(str(project_root))

from backend.mcp.client import call_tool


result = call_tool(
    server_url="http://localhost:9000",
    endpoint="find_nearby_schools",
    payload={
        "location": "Islamabad"
    }
)

print(result)