import requests

from backend.utils.logger import logger


def call_tool(
    server_url: str,
    endpoint: str,
    payload: dict
):

    try:

        response = requests.post(
            f"{server_url}/{endpoint}",
            json=payload,
            timeout=20
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        logger.error(
            f"MCP tool call failed: {str(e)}"
        )

        return {
            "error": str(e)
        }