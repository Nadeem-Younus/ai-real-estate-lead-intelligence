from backend.services.config import settings
from langfuse import get_client

# Force .env loading
_ = settings.LANGFUSE_PUBLIC_KEY

langfuse = get_client()