import requests

from backend.services.config import settings


class GooglePlacesService:

    BASE_URL = (
        "https://places.googleapis.com/v1/places:searchNearby"
    )

    @staticmethod
    def search_nearby(
        latitude: float,
        longitude: float,
        place_type: str,
        radius: int = 3000
    ):

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key":
                settings.GOOGLE_MAPS_API_KEY,

            "X-Goog-FieldMask":
                (
                    "places.displayName,"
                    "places.formattedAddress,"
                    "places.primaryType"
                )
        }

        payload = {
            "includedTypes": [
                place_type
            ],

            "maxResultCount": 5,

            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude": latitude,
                        "longitude": longitude
                    },
                    "radius": radius
                }
            }
        }

        response = requests.post(
            GooglePlacesService.BASE_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "places",
            []
        )
    


def geocode_location(location):
    url = (
        "https://maps.googleapis.com/maps/api/geocode/json"
        )

    response = requests.get(
        url, 
        params={
            "address": location,
            "key":
            settings.GOOGLE_MAPS_API_KEY
            }
        )

    data = response.json()

    if not data["results"]:
        return None

    loc = (
        data["results"][0]
        ["geometry"]
        ["location"]
    )

    return (
        loc["lat"],
        loc["lng"]
    )