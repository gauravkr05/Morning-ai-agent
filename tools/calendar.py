import os
import datetime
import json
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_today_schedule():
    creds = None
    creds_path = os.getenv("GOOGLE_CALENDAR_CREDENTIALS")
    token_path = os.getenv("GOOGLE_CALENDAR_TOKEN")

    # Load token if it exists
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    end_of_day = (datetime.datetime.utcnow().replace(hour=23, minute=59)).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary', timeMin=now, timeMax=end_of_day,
        maxResults=10, singleEvents=True, orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        return "No events scheduled today. You are free."

    schedule_summary = "Today's schedule:\n"
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        schedule_summary += f"- {start}: {summary}\n"

    return schedule_summary