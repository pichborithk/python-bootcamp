import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("PHONE_NUMBER")

owm_api_key = os.getenv("OWM_API_KEY")

# PARAMETERS = {"lat": "11.556374", "lon": "104.928207", "appid": api_key}
PARAMETERS = {"lat": "10.6267867", "lon": "103.5115545", "appid": owm_api_key}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=PARAMETERS
)

response.raise_for_status()

weather_data = response.json()

# for num in range(0, 3):
#     current_weather_id = weather_data["list"][num]["weather"][0]["id"]
#     if 500 <= current_weather_id < 700:
#         print("Bring your umbrella.")
#         break

# weather_data_today_list = weather_data["list"].slice(4)
# weather_data_today_list = weather_data["list"][0:4]

weather_data_today_list = weather_data["list"][:4]

for hour_data in weather_data_today_list:
    condition_code = hour_data["weather"][0]["id"]
    if 500 <= condition_code < 700:
        # print("Bring your umbrella.")
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            from_="+14065406948",
            to=phone_number,
            body="It's going to rain today. Remember to bring an umbrella",
        )
        print(message.status)
        break
