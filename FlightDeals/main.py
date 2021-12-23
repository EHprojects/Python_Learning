# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

ORIGIN_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()
# pprint(sheet_data)
# print()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])

# pprint(sheet_data)

# data_manager.update_sheet_data(sheet_data)

for row in sheet_data:
    flight = flight_search.get_flight_data(
        iata_from=ORIGIN_IATA,
        iata_to=row["iataCode"]
    )

    if flight is None:
        flight = flight_search.get_flight_data(
            iata_from=ORIGIN_IATA,
            iata_to=row["iataCode"],
            max_stops=1
        )
        if flight is None:
            pass

    if flight.price < row["lowestPrice"]:
        row["lowestPrice"] = flight.price
        notification_manager.send_notification(flight)


data_manager.update_sheet_data(sheet_data)
