import requests
import os
from flight_data import FlightData

KIWI_ENDPOINT = os.getenv("KIWI_ENDPOINT")
KIWI_HEADERS = {"apikey": os.getenv("KIWI_API_KEY")}


# class FlightSearch: #Might not need you class


# def get_destination_code(self, city_name):
def get_destination_code(city_name):
    query = {"term": city_name, "location_types": "city"}
    response = requests.get(
        url=f"{KIWI_ENDPOINT}/locations/query", headers=KIWI_HEADERS, params=query
    )
    data = response.json()["locations"]
    return data[0]["code"]


# def check_flights(self, origin_city_code, destination_city_code, date_from, date_to):
def check_flights(origin_city_code, destination_city_code, date_from, date_to):
    query = {
        "fly_from": origin_city_code,
        "fly_to": destination_city_code,
        "date_from": date_from.strftime("%d/%m/%Y"),
        "date_to": date_to.strftime("%d/%m/%Y"),
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 60,
        "one_for_city": 1,
        "curr": "USD",
        "max_stopovers": 0,
    }
    response = requests.get(
        url=f"{KIWI_ENDPOINT}/v2/search", headers=KIWI_HEADERS, params=query
    )

    try:
        data = response.json()["data"][0]
    except IndexError:

        query["max_stopovers"] = 1
        response = requests.get(
            url=f"{KIWI_ENDPOINT}/v2/search", headers=KIWI_HEADERS, params=query
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                depart_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
    else:
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            depart_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
