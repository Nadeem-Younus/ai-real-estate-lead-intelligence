from backend.tools.property_tools import PropertySearchTool

tool = PropertySearchTool()

result = tool._run(
    budget=30000000,
    property_type="House",
    location="Islamabad"
)
print(result)