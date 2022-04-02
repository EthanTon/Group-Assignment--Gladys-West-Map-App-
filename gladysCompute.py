import gladysSatellite as sat
def gpsAverage(x,y):
    """
    Calculate the average of the GPS coordinates
    """
    return (sat.gpsValue(x,y,"latitude")+sat.gpsValue(x,y,"longitude")+sat.gpsValue(x,y,"altitude")+sat.gpsValue(x,y,"time"))/4



# print(gpsAverage(0,0))