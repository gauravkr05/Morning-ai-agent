# Morning AI

Morning AI is an intelligent assistant that helps you start your day with the best possible activity, tailored to your environment and schedule. By integrating real-time weather and air quality data, your Google Calendar, and a customizable list of activities, the system uses a Large Language Model (LLM) to recommend the most suitable morning activity for you. The recommendation is then delivered directly to your email inbox.

## How It Works

1. **Data Collection**: The system gathers:
   - **Weather**: Current weather conditions for your city using the OpenWeatherMap API.
   - **Air Quality**: Real-time AQI (Air Quality Index) using the AirVisual API.
   - **Schedule**: Your day's events from Google Calendar to find free time slots.
   - **Activities**: A list of possible activities (with duration, distance, and type) from an Excel file (`activities.xlsx`).
2. **AI Recommendation**: All collected data is sent to a local LLM (default: Mistral via Ollama) which reasons step-by-step to select the optimal activity for today, considering weather, air quality, your availability, and the nature of each activity.
3. **Notification**: The chosen activity is emailed to you using your configured email credentials.

## Technologies Used
- **Python 3**
- **APIs**: OpenWeatherMap, AirVisual, Google Calendar
- **LLM**: Local model via [Ollama](https://ollama.com/) (default: Mistral, configurable)
- **Excel Parsing**: openpyxl
- **Email**: SMTP (Gmail by default)
- **Environment Management**: python-dotenv

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
    # Ollama (LLM)
    OLLAMA_BASE_URL=http://localhost:11434
    OLLAMA_MODEL=mistral
    ```
    - `WEATHER_API_KEY`: Get from [OpenWeatherMap](https://openweathermap.org/api).
    - `AQI_API_KEY`: Get from an AQI API provider.
    - `GOOGLE_CALENDAR_CREDENTIALS`: Your Google Calendar API credentials file. Follow the instructions [here](https://developers.google.com/calendar/api/quickstart/python) to get it.
    - `EMAIL_PASSWORD`: If using Gmail, you'll need to generate an "App Password".
    - `OLLAMA_BASE_URL` and `OLLAMA_MODEL`: (Optional) Configure your local LLM endpoint and model name.

5.  **Create `activities.xlsx`**: Create an Excel file named `activities.xlsx` in the root directory with the following columns (row 1 as headers):
    - `Name` (string): Name of the activity (e.g., Jogging)
    - `Duration` (number): Duration in minutes
    - `Distance` (number): Distance in kilometers (if applicable)
    - `Type` (string): Activity type (e.g., indoor, outdoor)
    
    Example:
    | Name     | Duration | Distance | Type   |
    |----------|----------|----------|--------|
    | Jogging  | 30       | 5        | outdoor|
    | Yoga     | 45       |          | indoor |

## Usage

Run the `main.py` script to get your personalized morning activity recommendation:
```bash
python main.py
```

## Notes
- The LLM runs locally via Ollama; ensure Ollama is installed and running, and the model specified in `.env` is available.
- All API keys and credentials must be valid for the system to function.
- The system is modular—APIs, LLM, and email settings can be swapped or extended as needed. 