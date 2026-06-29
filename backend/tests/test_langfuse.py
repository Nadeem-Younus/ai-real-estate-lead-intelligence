from langfuse import get_client
from backend.services.config import settings

print(settings.LANGFUSE_PUBLIC_KEY)
print(settings.LANGFUSE_HOST)

langfuse = get_client()

langfuse.create_event(
    name="test-event"
)

langfuse.flush()

print("Event sent")