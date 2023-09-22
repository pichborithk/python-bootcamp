# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
from flight_search import FlightSearch
from pprint import pprint

load_dotenv()

from data_manager import DataManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_code()