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
        self.sheety_put_endpoint = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/prices/[Object ID]"
        self.sheety_headers = {
            "Authorization": SHEETY_AUTH
        }

    def get_sheet_data(self):
        response = requests.get(url=self.sheety_get_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        return response.json()["prices"]
