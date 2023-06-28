from questdb.ingress import Sender
import datetime

sender = Sender("35.239.240.215", 9009)
sender.connect()

symbols = {"Airline": "DL", "Origin": "ABY", "OriginState": "GA", "Dest": "ATL", "DestState": "GA"}

columns = {"FlightDate": datetime.datetime(2018, 1, 23), "FlightNumber": 3298, "DepDelay": -5, "ArrDelay": -8, "Cancelled": False, "Diverted": False, "Distance": 145}

sender.row("Flights", symbols=symbols, columns=columns)

sender.flush()
