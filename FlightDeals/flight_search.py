import requests
import datetime
from dotenv import load_dotenv
import os
from flight_data import FlightData

load_dotenv("../.idea/.env")

KIWI_API_KEY = os.getenv("KIWI_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.kiwi_headers = {
            "apikey": KIWI_API_KEY
        }

    def get_iata_code(self, city_name):
        kiwi_iata_endpoint = "https://tequila-api.kiwi.com/locations/query"
        iata_params = {
            "term": city_name
        }
        response = requests.get(url=kiwi_iata_endpoint, headers=self.kiwi_headers, params=iata_params)
        response.raise_for_status()
        print(response.json()["locations"][0]["code"])
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def get_flight_data(self, iata_from, iata_to, max_stops=0):
        kiwi_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

        # fly_from - iata_from (from main.py)
        # fly_to - iata_to (from sheet_data)
        # date_from - add one day to current day?
        # date_to - datetime.timedelta()

        date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")  # tomorrow
        date_to = (datetime.datetime.now() + datetime.timedelta(days=(6 * 30))).strftime("%d/%m/%Y")  # 6 months

        search_params = {
            "fly_from": iata_from,  # Kiwi API ID of the departure location
            "fly_to": iata_to,  # Kiwi api ID of the arrival destination
            "max_stopovers": max_stops,  # max number of stopovers per itinerary
            "date_from": date_from,  # search flights from this date
            "date_to": date_to,  # search flights up to this date
            "nights_in_dst_from": 7,  # the minimal length of stay in the destination given in the fly_to parameter
            "nights_in_dst_to": 28,  # the maximal length of stay in the destination given in the fly_to parameter
            "curr": "GBP",  # use this parameter to change the currency in the response
            "sort": "price",  # sorts the results by quality, price, date or duration.
            "limit": 1,  # limit number of results; the default value is 200
        }

        response = requests.get(url=kiwi_search_endpoint, headers=self.kiwi_headers, params=search_params)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            print(f"{iata_to}: ??{data['price']}")
        except IndexError:
            print(f"No direct flights found for {iata_to}.")
            search_params["max_stopovers"] = 2
            response = requests.get(url=kiwi_search_endpoint, headers=self.kiwi_headers, params=search_params)

            try:
                data = response.json()["data"][0]
                print(f"{iata_to}: ??{data['price']}")
            except IndexError:
                print(f"No flights found for {iata_to}.")
                return None
            else:
                currency = response.json()["currency"]
                price = data["price"]
                depart_iata = data["route"][0]["flyFrom"]
                dest_iata = data["route"][1]["flyTo"]
                depart_city = data["route"][0]["cityFrom"]
                dest_city = data["route"][1]["cityTo"]
                airline = data["route"][0]["airline"]
                depart_date = data["route"][0]["local_departure"].split("T")[0]
                return_date = data["route"][2]["local_departure"].split("T")[0]
                stop_iata = data["route"][0]["flyTo"]
                stops = search_params["max_stopovers"]

                flight_data = FlightData(
                    currency=currency,
                    price=price,
                    depart_iata=depart_iata,
                    dest_iata=dest_iata,
                    depart_city=depart_city,
                    dest_city=dest_city,
                    airline=airline,
                    depart_date=depart_date,
                    return_date=return_date,
                    stop_overs=stops,
                    via_city=stop_iata
                )

                return flight_data

        else:
            currency = response.json()["currency"]
            price = data["price"]
            depart_iata = data["route"][0]["flyFrom"]
            dest_iata = data["route"][0]["flyTo"]
            depart_city = data["route"][0]["cityFrom"]
            dest_city = data["route"][0]["cityTo"]
            airline = data["route"][0]["airline"]
            depart_date = data["route"][0]["local_departure"].split("T")[0]
            return_date = data["route"][1]["local_departure"].split("T")[0]

            flight_data = FlightData(
                currency=currency,
                price=price,
                depart_iata=depart_iata,
                dest_iata=dest_iata,
                depart_city=depart_city,
                dest_city=dest_city,
                airline=airline,
                depart_date=depart_date,
                return_date=return_date
            )

            return flight_data
