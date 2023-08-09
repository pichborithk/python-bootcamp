import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = "graph1"

pixela_users_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_users_endpoint}/{USERNAME}/graphs"
pixela_pixel_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Make request to create user on pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

headers = {"X-USER-TOKEN": TOKEN}

# Make request to create graph for user on pixela
# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_data = {"date": today.strftime("%Y%m%d"), "quantity": "1.3"}

response = requests.post(url=pixela_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
