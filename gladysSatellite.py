from email.contentmanager import raw_data_manager
import json

#readSat collects data from the satellite. It requires a "call" such as altitude, latitude, etc. 
#file is read and data is returned as a list of dictionaries
def readSat(call):
    file_name = call+"-satellite.json"
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

    
#gpsValue takes x y coordinates and a call and reads the value
def gpsValue(x,y,call):
    data = readSat(call)
    #total amount of data is 100^2 
    return data[(x*100)+y]["value"]
