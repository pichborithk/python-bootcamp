import requests
import os

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_HEADERS = {"Authorization": f"Basic {SHEETY_TOKEN}"}


class DataManager:
    def __init__(self):
        self.users_data = []

    def add_user_data(self, first_name, last_name, email):
        new_data = {
            "user": {"firstName": first_name, "lastName": last_name, "email": email}
        }
        response = requests.post(
            url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS, json=new_data
        )
        print(response.text)
        self.users_data.append(new_data["user"])
        print("Success! Your email has been added.")
