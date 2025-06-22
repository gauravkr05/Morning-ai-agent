import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_aqi(city="Delhi") -> int:
    """
    Fetches AQI (US) value for the given city.
    """
    api_key = os.getenv("AQI_API_KEY")
    if not api_key:
        raise Exception("Missing AQI_API_KEY in .env file")

    url = f"http://api.airvisual.com/v2/city?city={city}&state=Delhi&country=India&key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch AQI data: {response.text}")

    data = response.json()
    if data.get("status") != "success":
        raise Exception("API returned unsuccessful status")

    return data["data"]["current"]["pollution"]["aqius"]