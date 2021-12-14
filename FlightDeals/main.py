# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint


data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_sheet_data()
pprint(sheet_data)

for row in sheet_data:
    row["city"]
    row["iataCode"] = flight_search.get_iata_code(row["city"])

pprint(sheet_data)
