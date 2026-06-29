from langfuse import get_client
from backend.services.config import settings

#print(settings.LANGFUSE_PUBLIC_KEY)
#print(settings.LANGFUSE_HOST)


langfuse = get_client()

with langfuse.start_as_current_observation(
    as_type="span",
    name="test-real-estate-trace"
):
    print("Running test trace")

langfuse.flush()

print("Trace sent")