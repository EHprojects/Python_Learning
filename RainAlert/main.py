import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient #  For PythonAnywhere hosting
from dotenv import load_dotenv

load_dotenv("../.idea/.env")


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
ACCT_ID = os.getenv("ACCT_ID")
AUTH_TOK = os.getenv("AUTH_TOK")
FROM_NUM = os.getenv("FROM_NUM")
TO_NUM = os.getenv("TO_NUM")
account_sid = ACCT_ID
auth_token = AUTH_TOK

# Open Weather Map Information
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))
OWM_API_KEY = os.getenv("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

twelve_hour = weather_data["hourly"][:12]

will_rain = False

for hour in twelve_hour:
    for obs in hour["weather"]:
        if obs["id"] < 700:
            will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()  # For PythonAnywhere hosting
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}  # For PythonAnywhere hosting
    # client = Client(account_sid, auth_token, http_client=proxy_client)  # For PythonAnywhere hosting
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="You need an umbrella today! ☂️",
        from_=FROM_NUM,
        to=TO_NUM
    )

    print(message.status)
