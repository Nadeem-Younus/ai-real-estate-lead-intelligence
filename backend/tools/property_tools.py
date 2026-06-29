import json

from pathlib import Path

from crewai.tools import BaseTool

from pydantic import BaseModel, Field


class PropertySearchInput(BaseModel):
    budget: int = Field(description="Maximum budget as integer only")

    property_type: str = Field(description="Property type")

    location: str = Field(description="City name")


class PropertySearchTool(BaseTool):

    name: str = "Property_Search"

    description: str = (
        """
        Search available properties.

        Required inputs:
        - budget (integer only, no commas, no PKR symbol)
        - property_type (House, Villa, Apartment, Shop, Office)
        - location (city name)

        Returns matching properties from the inventory.
        """
    )
    
    def _run(
        self,
        budget: int,
        property_type: str,
        location: str
    ):

        data_file = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "data"
            / "properties.json"
        )

        with open(
            data_file,
            "r",
            encoding="utf-8"
        ) as f:

            properties = json.load(f)

        matches = []

        for property_item in properties:

            if (
                property_item["price"] <= budget
                and property_item["type"].lower() == property_type.lower()
                and property_item["location"].lower() == location.lower()
            ):
                
                matches.append(property_item)

        return matches