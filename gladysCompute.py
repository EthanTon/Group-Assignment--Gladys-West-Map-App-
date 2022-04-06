
import gladysSatellite as sat


def gpsAverage(x, y):
    """
    Calculate the average of the GPS coordinates
    """
    return (sat.gpsValue(x, y, "latitude")+sat.gpsValue(x, y, "longitude")+sat.gpsValue(x, y, "altitude")+sat.gpsValue(x, y, "time"))/4


def gpsDistance(user_xpos, user_ypos, destination_xpos, destination_ypos):
    """
    Calculate the distance between two GPS coordinates
    """
    return (((gpsAverage(user_xpos, user_ypos)))**2 + (gpsAverage(destination_xpos, destination_ypos)**2))**0.5


# # print(gpsAverage(0,0))


# import io
# import math
# import gladysSatellite as satellite
# """
# Student: Zyed Ismailjee
# Module: gladysCompute
# Description: This module does ...
# """
# def gpsAverage(x1, y1, x2, y2):


#     """
#     document your function definition here. what does it do?
#     Calculates the disatance as the average between two points
#     """
#     """
#     delete the remaining code *in this function* and replace it with
#     your own code. add more code to do what the assignment asks of you.
#     """
#     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#     return dist

# print(gpsAverage(x1, y1, x2, y2))


# def distance(current, destination):
#     d1 = [4, 0]
#     d2 = [6, 6]


#     distance = math.sqrt(((d1[0]-d2[0])**2)+((d1[1]-d2[1])**2))

#     print(distance)

#     distance = gpsAverage(3, 4)
#     return distance



"""
"""
#import io
#import gladysSatellite as satellite
"""
Student: Gabriel Solomon
Module: gladysCompute
Description: This module does ...
"""
#def gpsAverage(x1,y1,x2,y2):
"""
document your function definition here. what does it do?
Calculates the disatance as the average between two points
"""
"""
delete the remaining code *in this function* and replace it with
your own code. add more code to do what the assignment asks of you.
"""
#dist    =   math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#return dist

#print gpsAverage(x1, y1, x2, y2)

"""
def distance(current, destination):
    d1  =   [4, 0]
    d2  =   [6, 6]
distance = math.sqrt( ((d1[0]-d2[0])**2)+((d1[1]-d2[1])**2) )

print(distance)
"""
#document your function definition here. what does it do?
"""
"""
#delete the remaining code *in this function* and replace it with
#your own code. add more code to do what the assignment asks of you.
"""
distance = gpsAverage(3, 4)
return distance
"""
