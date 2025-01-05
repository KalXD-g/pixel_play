import math
import cv2 as cv
import numpy as np

screen = np.zeros((600, 600, 3), dtype=np.uint8)  # height width channels

color_dictionary = {
    1: (0, 0, 255),    # Red
    2: (0, 155, 255),  # Orange
    3: (0, 255, 255),  # Yellow
    4: (0, 255, 0),    # Green
    5: (255, 0, 0),    # Blue
    6: (255, 0, 255)   # Purple
}

print('''
1->Red
2->Orange
3->Yellow
4->Green
5->Blue
6->Purple
''')

light_color = int(input("Choose the color of light::"))

wavelength_dictionary = {
    1: 620,  # Red
    2: 590,  # Orange
    3: 570,  # Yellow
    4: 495,  # Green
    5: 450,  # Blue
    6: 380   # Purple
}

#TODO Uncomment below line later (restrict taking 90 as input)
# incident_angle_deg = int(input("Incident angle (degrees)::"))

incident_angle_deg = 44.1243155255
incident_angle_rad = math.radians(incident_angle_deg)

# Refractive index of Upper medium
upper_refractive_index=float(input("Refractive Index of Upper medium::"))

# Refractive index of Upper medium
lower_refractive_index=float(input("Refractive Index of Lower medium::"))

#* Calculate Angle of Refraction (Result is in Radians)
refraction_angle=math.asin((upper_refractive_index/lower_refractive_index)*(math.sin(incident_angle_rad)))

# Fill bottom part with color

for x in range(600):
    for y in range(600):
        if x>300:
            screen[x][y]=[51,42,34] # 142 175 210

# Centre Point
centre_point = (300, 300)

# Reference Point to calculate the other coordinate for incident ray
upper_reference_point = (300, 0)

# Reference Point to calculate the other coordinate for refracted ray
lower_reference_point = (300,600)

def calculate_y(angle):
    length = (upper_reference_point[1] - centre_point[1]) * math.tan(angle)
    return int(length)

#! Originally planned to adjust the y-coordinate by 1 due to pixel rounding errors, but decided to ignore it for simplicity.
calculated_point_incident_ray = (upper_reference_point[0] + int((upper_reference_point[1]-centre_point[1])*math.tan(incident_angle_rad)), upper_reference_point[1])

# Calculating endpoint for refracted ray
calculated_point_refracted_ray=(lower_reference_point[0] + int((lower_reference_point[1]-centre_point[1])*math.tan(refraction_angle)), lower_reference_point[1])

# Calculating the endpoint for the reflected ray
calculated_point_reflected_ray = (upper_reference_point[0] - calculate_y(incident_angle_rad), upper_reference_point[1])

# Lines Part
cv.line(screen, (300, 0), (300, 600), (105, 105, 105), 1)  # normal line
cv.line(screen, (0, 300), (600, 300), (255, 255, 255), 1)  # media separator
cv.line(screen, centre_point, calculated_point_incident_ray, color_dictionary[light_color], 1)
cv.line(screen, centre_point, calculated_point_reflected_ray, color_dictionary[light_color], 1)
cv.line(screen, centre_point, calculated_point_refracted_ray, color_dictionary[light_color], 1)

# Text part
u_text=f"n1={upper_refractive_index}"
l_text=f"n2={lower_refractive_index}"
r_text = f"{(math.degrees(refraction_angle)):.5f}"
i_text=f"{(incident_angle_deg):.5f}"
cv.putText(screen, u_text,(80,250),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
cv.putText(screen, l_text,(80,350),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
cv.putText(screen, "Angle of Refraction=",(50,500),cv.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)
cv.putText(screen, r_text,(50,520),cv.FONT_HERSHEY_SIMPLEX,0.35,(0,255,255),1)
cv.putText(screen, "Angle of Incidence=",(50,100),cv.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)
cv.putText(screen, str(incident_angle_deg),(50,120),cv.FONT_HERSHEY_SIMPLEX,0.35,(0,255,255),1)

# X -X Y -Y
cv.putText(screen, "X",(590,290),cv.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)
cv.putText(screen, "-X",(10,290),cv.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)
cv.putText(screen, "Y",(310,10),cv.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)
cv.putText(screen, "-Y",(310,590),cv.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)


if screen is None:
    raise ValueError("Image not found")

cv.imshow('Snell\'s Law Visualizer', screen)

while True:
    if cv.waitKey(1) & 0xFF == 32:
        break

cv.destroyAllWindows()