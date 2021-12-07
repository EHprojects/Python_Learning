import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient #  For PythonAnywhere hosting
from dotenv import load_dotenv

load_dotenv("../.idea/.env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alphavantage
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv("AV_API_KEY")

# News API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Twilio
TWIL_ACCT_ID = os.getenv("TWIL_ACCT_ID")
TWIL_AUTH_TOK = os.getenv("TWIL_AUTH_TOK")
TWIL_FROM_NUM = os.getenv("TWIL_FROM_NUM")
TWIL_TO_NUM = os.getenv("TWIL_TO_NUM")
account_sid = TWIL_ACCT_ID
auth_token = TWIL_AUTH_TOK

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

close_change = close_data[0] - close_data[1]
pct_change = round(close_change / close_data[1] * 100, 2)

if abs(pct_change) >= 0.01:  # Change to desired %

    news_parameters = {
        "q": f'"{STOCK}"',
        "language": "en",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_data = news_data["articles"]

    change_dir = None
    if pct_change < 0:
        change_dir = "🔻"
    else:
        change_dir = "🔺"

    for article in news_data:
        title = article["title"]
        desc = article["description"]
        # print(f"{STOCK}: {change_dir}{pct_change}%\nHeadline: {title}\nBrief: {desc}")

        # proxy_client = TwilioHttpClient()  # For PythonAnywhere hosting
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}  # For PythonAnywhere hosting
        # client = Client(account_sid, auth_token, http_client=proxy_client)  # For PythonAnywhere hosting
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"{STOCK}: {change_dir}{pct_change}%\nHeadline: {title}\nBrief: {desc}",
            from_=TWIL_FROM_NUM,
            to=TWIL_TO_NUM
        )

        print(message.status)
