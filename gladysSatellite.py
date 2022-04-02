from email.contentmanager import raw_data_manager
import json


def readSat():
    with open("altitude-satellite.json", "r") as f:
        satData_alt = json.load(f)
    with open("latitude-satellite.json", "r") as f:
        satData_lat = json.load(f)
    with open("longitude-satellite.json", "r") as f:
        satData_long = json.load(f)
    with open("time-satellite.json", "r") as f:
        satData_time = json.load(f)
    return satData_alt, satData_lat, satData_long, satData_time

def gpsValue(x,y,call):
    if call == "altitude":
        return readSat()[0][x][y]
    elif call == "latitude":
        return readSat()[1][x][y]
    elif call == "longitude":
        return readSat()[2][x][y]
    elif call == "time":
        return readSat()[3][x][y]


print(gpsValue(0,0,"altitude"))
    



print(readSat())