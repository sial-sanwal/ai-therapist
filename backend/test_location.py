import googlemaps
from config import GOOGLE_MAP_API_KEY

gmaps=googlemaps.Client(key=GOOGLE_MAP_API_KEY)

 
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    geocode_result=gmaps.geocode(location)
    print(geocode_result)

find_nearby_therapists_by_location("New york")