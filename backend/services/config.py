import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # OpenAI
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    # Google Maps
    GOOGLE_MAPS_API_KEY = os.getenv(
        "GOOGLE_MAPS_API_KEY"
    )

    # Langfuse
    LANGFUSE_PUBLIC_KEY = os.getenv(
        "LANGFUSE_PUBLIC_KEY"
    )

    LANGFUSE_SECRET_KEY = os.getenv(
        "LANGFUSE_SECRET_KEY"
    )

    LANGFUSE_HOST = os.getenv(
        "LANGFUSE_HOST",
        "https://cloud.langfuse.com"
    )

    # MCP Servers
    MAPS_MCP_URL = os.getenv(
        "MAPS_MCP_URL",
        "http://localhost:9000"
    )

    BREVO_MCP_URL = os.getenv(
        "BREVO_MCP_URL",
        "http://localhost:9001"
    )

    # Brevo
    BREVO_API_KEY = os.getenv(
        "BREVO_API_KEY"
    )

    BREVO_SENDER_EMAIL = os.getenv(
        "BREVO_SENDER_EMAIL"
    )

    BREVO_SENDER_NAME = os.getenv(
        "BREVO_SENDER_NAME",
        "AI Real Estate Lead Intelligence"
    )

    # App
    APP_MODE = os.getenv(
        "APP_MODE",
        "demo"
    )


settings = Settings()