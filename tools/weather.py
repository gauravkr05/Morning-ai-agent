import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_summary(city="Delhi") -> str:
    """
    Fetches weather forecast for the given city and formats it into a summary string.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise Exception("Missing WEATHER_API_KEY in .env file")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather data: {response.text}")

    data = response.json()

    weather_desc = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    summary = (
        f"Weather in {city}:\n"
        f"- Condition: {weather_desc}\n"
        f"- Temperature: {temp}°C\n"
        f"- Humidity: {humidity}%\n"
        f"- Wind Speed: {wind} m/s"
    )

    return summary