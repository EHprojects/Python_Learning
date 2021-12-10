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

# excercise_input = input("What did you do today, guy?")

ntx_params = {
    "query": "did 60 pushups and ran 3 miles",
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 185.5,
    "age": 30
}

# response = requests.post(url=ntx_endpoint, headers=ntx_headers, json=ntx_params)
# # print(response)
# ntx_result = response.json()
# # print(ntx_result["exercises"])
#
# # Need: Date, Time, Exercise ('name'), Duration('duration_min'), Calories ('nf_calories')
#
# # print(ntx_result["exercises"][0])
#
# sheety_post_endpoint = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/workoutTracking/workouts"
#
# sheety_headers = {
#     "Authorization": SHEETY_AUTH
# }
#
# # for result in ntx_result["exercises"]:
# #     print(result["name"])
# #     print(result["duration_min"])
# #     print(result["nf_calories"])
#
# sheety_test_json = {
#     "workout": {
#         "date": "12/9/2021",
#         "time": "21:00",
#         "exercise": "push-up",
#         "duration": "3",
#         "calories": "13.43"
#     }
# }
#
# sheety_response = requests.post(url=sheety_post_endpoint, headers=sheety_headers, json=sheety_test_json)
# print(sheety_response)



today = datetime.now()
print(today.strftime("%Y%m%d"))

