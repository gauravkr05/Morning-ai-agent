from tools.weather import get_weather_summary
from tools.aqi import get_aqi
from tools.calendar import get_today_schedule
from tools.excel import get_activities_from_excel
from tools.llm import call_llm
from tools.emailer import send_email

def main():
    print("🔄 Collecting data from tools...")

    # Get inputs from tools
    weather_data = get_weather_summary()
    aqi_value = get_aqi()
    schedule = get_today_schedule()
    activities = get_activities_from_excel()

    print("✅ All data collected. Sending to LLM...")

    # Let LLM decide the activity
    decision = call_llm(
        weather=weather_data,
        aqi=aqi_value,
        calendar_schedule=schedule,
        activities=activities
    )

    print("🧠 LLM decision received:", decision)

    # Send the decision by email
    send_email("Your Morning Activity Recommendation", decision)
    print("📧 Email sent!")

if __name__ == "__main__":
    main()