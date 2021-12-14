import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("../.idea/.env")

KIWI_API_KEY = os.getenv("KIWI_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    def get_iata_code(self, city_name):
        return "TESTING"

