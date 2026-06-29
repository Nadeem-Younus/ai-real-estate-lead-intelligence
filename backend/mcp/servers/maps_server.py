from fastapi import FastAPI

from backend.services.maps_service import (
    GooglePlacesService,
    geocode_location
)

app = FastAPI()

# Schools Endpoint
@app.post(
    "/find_nearby_schools"
)
def find_nearby_schools(
    payload: dict
):

    location = payload["location"]

    lat, lng = (
        geocode_location(location)
    )

    return GooglePlacesService.search_nearby(
        lat,
        lng,
        "school"
    )

#Hospitals Endpoint
@app.post(
    "/find_nearby_hospitals"
)
def find_nearby_hospitals(
    payload: dict
):

    lat, lng = geocode_location(
        payload["location"]
    )

    return GooglePlacesService.search_nearby(
        lat,
        lng,
        "hospital"
    )

# Park Endpoint
@app.post(
    "/find_nearby_parks"
)
def find_nearby_parks(
    payload: dict
):

    lat, lng = geocode_location(
        payload["location"]
    )

    return GooglePlacesService.search_nearby(
        lat,
        lng,
        "park"
    )

# Shopping Malls Endpoint
@app.post(
    "/find_nearby_malls"
)
def find_nearby_malls(
    payload: dict
):

    lat, lng = geocode_location(
        payload["location"]
    )

    return GooglePlacesService.search_nearby(
        lat,
        lng,
        "shopping_mall"
    )

# Metro Stations Endpoint
@app.post(
    "/find_nearby_metro"
)
def find_nearby_metro(
    payload: dict
):

    lat, lng = geocode_location(
        payload["location"]
    )

    return GooglePlacesService.search_nearby(
        lat,
        lng,
        "subway_station" # Google supports subway_station as a place type.
    )


