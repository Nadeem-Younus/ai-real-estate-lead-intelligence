from backend.mcp.client import call_tool

result = call_tool(
    server_url="http://localhost:9000",
    endpoint="find_nearby_schools",
    payload={
        "location": "Islamabad"
    }
)

print(result)