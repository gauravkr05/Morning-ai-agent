import os
import subprocess
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

def call_llm(weather, aqi, calendar_schedule, activities):
    """
    Sends raw context to the LLM and asks it to decide the best activity.
    """
    prompt = f"""
You are a smart morning assistant. Your job is to pick the best physical activity for the user today.

Here is the data:
- Weather Forecast: {weather}
- Air Quality Index (AQI): {aqi}
- Calendar Schedule (free/busy time): {calendar_schedule}
- Available Activities (with duration and distance): {json.dumps(activities, indent=2)}

Think step-by-step:
1. Understand if the weather or air quality impacts any outdoor activities.
2. Understand the user's available free time from the calendar.
3. Consider which activity is most suitable today.
4. Pick the most optimal activity and time.
5. Give your final recommendation clearly in 1-2 lines.

Just return your final recommendation message. Do not explain or repeat the data.
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        return f"Error from LLM: {e.stderr}"