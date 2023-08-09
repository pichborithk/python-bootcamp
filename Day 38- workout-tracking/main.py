import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercises_text = input("Tell me which exercises you did: ")

headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY, "x-remote-user-id": "0"}

exercises_data = {
    "query": exercises_text,
    "gender": "male",
    "weight_kg": 120,
    "height_cm": 176,
    "age": 34,
}

response = requests.post(url=nutritionix_endpoint, json=exercises_data, headers=headers)
print(response.json())
