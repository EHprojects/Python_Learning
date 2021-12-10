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

ntx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

ntx_headers = {
    "x-app-id": NTX_APP_ID,
    "x-app-key": NTX_APP_KEY,
    "x-remote-user-id": "0"
}

excercise_input = input("What exercises did you do today?")

ntx_params = {
    "query": excercise_input,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 185.5,
    "age": 30
}

response = requests.post(url=ntx_endpoint, headers=ntx_headers, json=ntx_params)
ntx_result = response.json()

sheety_post_endpoint = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/workoutTracking/workouts"

sheety_headers = {
    "Authorization": SHEETY_AUTH
}

today = datetime.now()

for result in ntx_result["exercises"]:
    sheety_json = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_post_endpoint, headers=sheety_headers, json=sheety_json)
    print(sheety_response)



