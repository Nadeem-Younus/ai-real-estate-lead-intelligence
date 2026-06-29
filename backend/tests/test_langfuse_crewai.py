from langfuse import get_client
from backend.services.config import settings

langfuse = get_client()

with langfuse.start_as_current_observation(
    as_type="span",
    name="crewai-simple-test"
):
    print("Inside CrewAI test")

langfuse.flush()

print("Done")