class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, currency, price, depart_iata, dest_iata,
                 depart_city, dest_city, airline, depart_date, return_date, stop_overs=0, via_city=""):
        self.currency = currency
        self.price = price
        self.depart_iata = depart_iata
        self.dest_iata = dest_iata
        self.depart_city = depart_city
        self.dest_city = dest_city
        self.airline = airline
        self.depart_date = depart_date
        self.return_date = return_date



