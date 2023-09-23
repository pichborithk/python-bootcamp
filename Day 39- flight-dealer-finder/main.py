# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv

load_dotenv()

from datetime import datetime, timedelta
from data_manager import DataManager

# from flight_search import FlightSearch
from flight_search import get_destination_code, check_flights
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30))

# flight_search = FlightSearch()

notification_manager = NotificationManager()


for row in sheet_data:
    if row["iataCode"] == "":
        # row["iataCode"] = flight_search.get_destination_code(row["city"])
        row["iataCode"] = get_destination_code(row["city"])
        data_manager.update_destination_code(
            city_id=row["id"], city_code=row["iataCode"]
        )


for row in sheet_data:
    # flight = flight_search.check_flights(
    flight = check_flights(
        origin_city_code="LON",
        destination_city_code=row["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_now,
    )

    if flight.price < row["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} "
            f"to fly from {flight.origin_city}-{flight.origin_airport} "
            f"to {flight.destination_city}-{flight.destination_airport}, "
            f"from {flight.out_date} to {flight.return_date}."
        )
