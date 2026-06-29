import requests

response = requests.post(
    "http://127.0.0.1:9001/generate_followup_email",
    json={
        "customer_name": "John Smith",
        "property_name": "Luxury Villa Islamabad"
    }
)

print(response.status_code)
print(response.json())