import requests
import os

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_HEADERS = {"Authorization": f"Basic {SHEETY_TOKEN}"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self, city_id, city_code):
        new_data = {"price": {"iataCode": city_code}}
        response = requests.put(
            url=f"{SHEETY_ENDPOINT}/{city_id}",
            headers=SHEETY_HEADERS,
            json=new_data,
        )
        print(response.text)
