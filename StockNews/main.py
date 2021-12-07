import requests
import os
import math
from datetime import datetime
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient #  For PythonAnywhere hosting
from dotenv import load_dotenv

load_dotenv("../.idea/.env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv("AV_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=alpha_parameters)
response.raise_for_status()
stock_data = response.json()
daily_data = stock_data["Time Series (Daily)"]
dates = list(daily_data.keys())
last_two_dates = dates[:2]

close_data = []
for date in last_two_dates:
    close_data.append(float(daily_data[date]["4. close"]))

# print(close_data)

close_change = close_data[0] - close_data[1]
pct_change = round(close_change / close_data[1] * 100, 2)
# print(pct_change)

if abs(pct_change) >= 5:
    print("Get News")

