from email.contentmanager import raw_data_manager
import json


def readSat(call):
    file_name = call+"-satellite.json"
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

    

def gpsValue(x,y,call):
    data = readSat(call)
    #total amount of data is 99^2
    # print(data[(x*100)+y])
    return data[(x*100)+y]["value"]
