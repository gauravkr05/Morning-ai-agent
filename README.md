# Morning AI

This project uses AI to recommend a morning activity based on weather, air quality, your schedule, and a predefined list of activities. The recommendation is then sent to you via email.

## Features

- **Weather Summary**: Fetches the current weather for a specified city.
- **Air Quality Index (AQI)**: Fetches the current AQI for a specified city.
- **Google Calendar Integration**: Fetches your schedule for the day from your primary Google Calendar.
- **Activity Suggestions**: Reads a list of potential activities from an Excel file.
- **AI-Powered Recommendations**: Uses a Large Language Model (LLM) to decide the best activity.
- **Email Notifications**: Sends the final recommendation to your email address.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/morning-ai.git
    cd morning-ai
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

4.  **Create a `.env` file** in the root directory and add the following environment variables:

    ```env
    # Weather API
    WEATHER_API_KEY=your_openweathermap_api_key

    # AQI API
    AQI_API_KEY=your_aqi_api_key

    # Google Calendar API
    GOOGLE_CALENDAR_CREDENTIALS=path/to/your/credentials.json
    GOOGLE_CALENDAR_TOKEN=token.json

    # Email
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password
    EMAIL_RECIPIENT=recipient_email@example.com
    ```
    - `WEATHER_API_KEY`: Get from [OpenWeatherMap](https://openweathermap.org/api).
    - `AQI_API_KEY`: Get from an AQI API provider.
    - `GOOGLE_CALENDAR_CREDENTIALS`: Your Google Calendar API credentials file. Follow the instructions [here](https://developers.google.com/calendar/api/quickstart/python) to get it.
    - `EMAIL_PASSWORD`: If using Gmail, you'll need to generate an "App Password".

5.  **Create `activities.xlsx`**: Create an Excel file named `activities.xlsx` in the root directory with the following columns: `Name`, `Duration`, `Distance`.

## Usage

Run the `main.py` script to get your personalized morning activity recommendation:
```bash
python main.py
``` 