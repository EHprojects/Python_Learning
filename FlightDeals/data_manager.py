import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("../.idea/.env")

# Sheety API
SHEETY_AUTH = os.getenv("SHEETY_AUTH")


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.sheety_get_endpoint = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/prices"
        self.sheety_put_endpoint = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/prices/"
        self.sheety_headers = {
            "Authorization": SHEETY_AUTH
        }
        self.sheet_data = {}

    def get_sheet_data(self):
        response = requests.get(url=self.sheety_get_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        return response.json()["prices"]

    def update_sheet_data(self, sheet_data):
        for row in sheet_data:
            put_data = {
                "price": {
                    "city": row["city"],
                    "iataCode": row["iataCode"],
                    "lowestPrice": row["lowestPrice"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/prices/{row['id']}",
                                    headers=self.sheety_headers, json=put_data)
            print(response)

