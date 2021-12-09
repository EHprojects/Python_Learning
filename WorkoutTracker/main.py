import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("../.idea/.env")

# Nutritionix API
NTX_APP_ID = os.getenv("NTX_APP_ID")
NTX_APP_KEY = os.getenv("NTX_APP_KEY")

# Sheety API
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

ntx_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"

ntx_headers = {
    "x-app-id": NTX_APP_ID,
    "x-app-key": NTX_APP_KEY,
    "x-remote-user-id": "0"
}

# excercise_input = input("What did you do today, guy?")

ntx_params = {
    "query": "ran 3 miles",
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 185.5,
    "age": 30
}

response = requests.post(url=ntx_exercise, headers=ntx_headers, json=ntx_params)
print(response)
print(response.json())
