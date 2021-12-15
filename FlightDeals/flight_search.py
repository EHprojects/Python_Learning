import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("../.idea/.env")

KIWI_API_KEY = os.getenv("KIWI_API_KEY")

kiwi_endpoint = "https://tequila-api.kiwi.com/locations/query"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.kiwi_headers = {
            "apikey": KIWI_API_KEY
        }

    def get_iata_code(self, city_name):
        iata_params = {
            "term": city_name
        }
        response = requests.get(url=kiwi_endpoint, headers=self.kiwi_headers, params=iata_params)
        response.raise_for_status()
        print(response.json()["locations"][0]["code"])
        iata_code = response.json()["locations"][0]["code"]
        return iata_code



