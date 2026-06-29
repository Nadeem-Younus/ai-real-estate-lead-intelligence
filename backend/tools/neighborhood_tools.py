from crewai.tools import BaseTool

from backend.mcp.client import call_tool
from backend.services.config import settings


class NeighborhoodIntelligenceTool(BaseTool):

    name: str = "Neighborhood Intelligence Tool"

    description: str = """
    Retrieve nearby schools, hospitals,
    parks, shopping malls and metro stations
    for a given location.
    """

    def _run(
        self,
        location: str
    ):

        schools = call_tool(
            server_url=settings.MAPS_MCP_URL,
            endpoint="find_nearby_schools",
            payload={
                "location": location
            }
        )

        hospitals = call_tool(
            server_url=settings.MAPS_MCP_URL,
            endpoint="find_nearby_hospitals",
            payload={
                "location": location
            }
        )

        parks = call_tool(
            server_url=settings.MAPS_MCP_URL,
            endpoint="find_nearby_parks",
            payload={
                "location": location
            }
        )

        malls = call_tool(
            server_url=settings.MAPS_MCP_URL,
            endpoint="find_nearby_malls",
            payload={
                "location": location
            }
        )

        metro = call_tool(
            server_url=settings.MAPS_MCP_URL,
            endpoint="find_nearby_metro",
            payload={
                "location": location
            }
        )

        return {
            "schools": schools,
            "hospitals": hospitals,
            "parks": parks,
            "malls": malls,
            "metro": metro
        }