import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.715911498873375  # Your latitude
MY_LONG = -117.16154411424083  # Your longitude
MY_EMAIL = "email address"
MY_PASSWORD = "password"


# Your position is within +5 or -5 degrees of the ISS position.
def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # UTC Time Offset (UTC to PST): UTC-8:00

    # time_now = datetime.now()
    utc_time_now = datetime.utcnow()

    if utc_time_now.hour < sunrise or utc_time_now.hour > sunset:
        return True
    else:
        return False


def send_email_notification():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:The ISS is Overhead!\n\nLook up!")


while True:
    if iss_close() and is_dark():
        # send_email_notification()
        print(datetime.now())
        print("The ISS is passing overhead!")

    time.sleep(60)
