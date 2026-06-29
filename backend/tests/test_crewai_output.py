from backend.crews.real_estate_crew import RealEstateCrew

crew = RealEstateCrew()

result = crew.run(
    customer_name="John Smith",
    budget=30000000,
    property_type="House",
    timeline="30 days",
    location="Islamabad"
)

print(type(result))
print("\n=== LEAD ANALYSIS ===")
print(result["lead_analysis"])

print("\n=== PROPERTIES ===")
print(result["property_recommendations"])

print("\n=== MARKET ===")
print(result["neighborhood_intelligence"])

print("\n=== EMAIL ===")
print(result["followup_email"])