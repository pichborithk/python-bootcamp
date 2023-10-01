from dotenv import load_dotenv

load_dotenv()

from datetime import datetime, timedelta
from data_manager import DataManager

from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30))

notification_manager = NotificationManager()

for row in sheet_data:
    if row["iataCode"] == "":
        # row["iataCode"] = flight_search.get_destination_code(row["city"])
        row["iataCode"] = FlightSearch.get_destination_code(row["city"])
        DataManager.update_destination_code(
            city_id=row["id"], city_code=row["iataCode"]
        )

for row in sheet_data:
    # flight = flight_search.check_flights(
    flight = FlightSearch.check_flights(
        origin_city_code="LON",
        destination_city_code=row["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_now,
    )

    if flight is None:
        continue

    if flight.price < row["lowestPrice"]:
        message_content = f"Low price alert! Only ${flight.price} "
        f"to fly from {flight.origin_city}-{flight.origin_airport} "
        f"to {flight.destination_city}-{flight.destination_airport}, "
        f"from {flight.depart_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message_content += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # print(message_content)
        # notification_manager.send_sms(message_content=message_content)
        notification_manager.send_emails(email_content=message_content)
