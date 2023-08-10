import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
TOKEN = os.getenv("SHEETY_TOKEN")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = (
    "https://api.sheety.co/0f19e90cd91ebef484653657b6ae2102/workoutTracking/workouts"
)

exercises_text = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

sheety_headers = {"Authorization": f"Bearer {TOKEN}"}

exercises_data = {
    "query": exercises_text,
    "gender": "male",
    "weight_kg": 120,
    "height_cm": 176,
    "age": 34,
}

response = requests.post(
    url=nutritionix_endpoint, json=exercises_data, headers=nutritionix_headers
)
result = response.json()

today = datetime.now()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(
        url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers
    )
    # sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))
    print(sheety_response.text)
