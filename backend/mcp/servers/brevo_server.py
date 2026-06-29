import requests
from fastapi import FastAPI
from backend.services.config import settings


app = FastAPI(
    title="Brevo MCP Server"
)


@app.post("/generate_followup_email")
def generate_followup_email(payload: dict):

    customer_name = payload.get(
        "customer_name",
        "Customer"
    )

    property_name = payload.get(
        "property_name",
        "Property"
    )

    return {
        "subject": f"Regarding {property_name}",
        "body": f"""
Hello {customer_name},

Thank you for your interest in {property_name}.

We would be happy to arrange a viewing.

Please let us know your availability.

Best Regards,
AI Real Estate Lead Intelligence
"""
    }


@app.post("/send_email")
def send_email(payload: dict):

    print("EMAIL REQUEST RECEIVED")
    print(payload)

    to_email = payload["to_email"]
    subject = payload["subject"]
    body = payload["body"]

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json"
    }

    data = {
        "sender": {
            "name": "AI Real Estate Lead Intelligence",
            "email": settings.BREVO_SENDER_EMAIL
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "htmlContent": body.replace("\n", "<br>")
    }

    response = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        headers=headers,
        json=data,
        timeout=30
    )

    return response.json()