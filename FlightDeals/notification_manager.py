from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

load_dotenv("../.idea/.env")

# Twilio
TWIL_ACCT_ID = os.getenv("TWIL_ACCT_ID")
TWIL_AUTH_TOK = os.getenv("TWIL_AUTH_TOK")
TWIL_FROM_NUM = os.getenv("TWIL_FROM_NUM")
TWIL_TO_NUM = os.getenv("TWIL_TO_NUM")

# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, flight):
        client = Client(TWIL_ACCT_ID, TWIL_AUTH_TOK)

        if flight.stop_overs > 1:
            message = client.messages.create(
                body=f"Low price alert! Only £{flight.price} to fly from {flight.depart_city}-{flight.depart_iata} to "
                     f"{flight.dest_city}-{flight.dest_iata}, from {flight.depart_date} to {flight.return_date}."
                     f"\nFlight has 1 stop over, via {flight.via_city}",
                from_=TWIL_FROM_NUM,
                to=TWIL_TO_NUM
            )
        else:
            message = client.messages.create(
                body=f"Low price alert! Only £{flight.price} to fly from {flight.depart_city}-{flight.depart_iata} to "
                     f"{flight.dest_city}-{flight.dest_iata}, from {flight.depart_date} to {flight.return_date}.",
                from_=TWIL_FROM_NUM,
                to=TWIL_TO_NUM
            )

    def send_email(self, flight):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL_ADDR, EMAIL_PASS)
            if flight.stop_overs > 1:
                connection.sendmail(from_addr=EMAIL_ADDR,
                                    to_addrs=EMAIL_ADDR,
                                    msg=f"Low price alert! Only £{flight.price} to fly from {flight.depart_city}-"
                                        f"{flight.depart_iata} to {flight.dest_city}-{flight.dest_iata}, from "
                                        f"{flight.depart_date} to {flight.return_date}.\nFlight has 1 stop over, "
                                        f"via {flight.via_city}".encode('utf-8'))
            else:
                connection.sendmail(from_addr=EMAIL_ADDR,
                                    to_addrs=EMAIL_ADDR,
                                    msg=f"Low price alert! Only £{flight.price} to fly from {flight.depart_city}-"
                                        f"{flight.depart_iata} to {flight.dest_city}-{flight.dest_iata}, from "
                                        f"{flight.depart_date} to {flight.return_date}.")
