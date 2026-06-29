from backend.crews.real_estate_crew import (
    RealEstateCrew
)

crew = RealEstateCrew()

result = crew.run(
    customer_name="John Smith",
    budget=300000,
    property_type="Villa",
    timeline="30 days",
    location="Islamabad"
)

print(result)