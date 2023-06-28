from questdb.ingress import Sender
import sys, csv
from datetime import datetime

host = sys.argv[1]
port = int(sys.argv[2])
file = sys.argv[3]

with open(file, mode ='r') as file, Sender(host, port) as sender:
	csvFile = csv.reader(file)
	header = True
	for line in csvFile:
		if header:
			header = False
		else:
			symbols = {
				"Airline": line[9], 
				"Origin": line[23], 
				"OriginState": line[25], 
				"Dest": line[32], 
				"DestState": line[34]
			}
			columns = {
				"FlightDate": datetime.strptime(line[5], '%Y-%m-%d'), 
				"FlightNumber": int(line[19]), 
				"DepDelay": float(line[40]) if line[40] != '' else 0, 
				"ArrDelay": float(line[51]) if line[51] != '' else 0, 
				"Cancelled": True if line[56] == 0 else False, 
				"Diverted": True if line[58] == 0 else False, 
				"Distance": float(line[63])
			}
			sender.row("Flights", symbols=symbols, columns=columns)
	sender.flush()

