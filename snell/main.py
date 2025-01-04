import math
import cv2 as cv
import numpy as np

screen = np.zeros((512, 512, 3), dtype=np.uint8) # height width channels 


#TODO Uncomment below line later (restric taking 90 as input)
# incident_angle_deg=int(input("Incident angle (degrees)::"))

incident_angle_deg=30
incident_angle_rad=math.radians(incident_angle_deg)

# Centre Point
centre_point=(256,350)

# Reference Point to calculate the other coordiante
reference_point=(256,0)

def calculate_y():
    length=(reference_point[1]-centre_point[1])*math.tan(incident_angle_rad)
    return int(length)

#! The original idea was to add 1 to y-coordinate of calculated_point because the resultant line will be off by some pixels which is the resultant of flooring the length calculated from calculate_y() function. Different angles require different amount of compensation so I decided to ignore it completely
calculated_point=(reference_point[0]+calculate_y(), reference_point[1])

# Calculating end point for reflected ray
calculated_point_reflected_ray=(reference_point[0]-calculate_y(), reference_point[1])

cv.line(screen, (256,0),(256,512),(105,105,105),1) # normal line
cv.line(screen, (0,350),(512,350),(255,255,255),1) # media separator
cv.line(screen, centre_point, calculated_point, (0,255,0),1)
cv.line(screen, centre_point, calculated_point_reflected_ray, (0,255,0),1)

if screen is None:
    raise ValueError("Image not found")

cv.imshow('Snell\'s Law Visualizer', screen)

while True:
    if cv.waitKey(1) & 0xFF==32:
        break

cv.destroyAllWindows()