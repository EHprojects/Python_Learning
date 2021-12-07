import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("../.idea/.env")

PIX_API_TOKEN = os.getenv("PIX_API_TOKEN")
PIX_USER_NAME = os.getenv("PIX_USER_NAME")
PIX_GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIX_API_TOKEN,
    "username": PIX_USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIX_USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Water Consumption",
    "unit": "mL",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIX_API_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

pixel_creation_endpoint = f"{graph_endpoint}/{PIX_GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2021, month=12, day=6)

# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3100",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response)

update_date = datetime(year=2021, month=12, day=6).strftime("%Y%m%d")
update_endpoint = f"{graph_endpoint}/{PIX_GRAPH_ID}/{update_date}"
# update_endpoint = f"https://pixe.la/v1/users/{PIX_USER_NAME}/graphs/{PIX_GRAPH_ID}/{update_date}"

update_pixel_data = {
    "quantity": "3000"
}

# response = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)
# print(response)

# DELETE /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
response = requests.delete(url=update_endpoint, headers=headers)
print(response)
