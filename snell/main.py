import math
import cv2 as cv
import numpy as np
import time

color_map = {
    1: (0, 0, 255),
    2: (0, 155, 255),
    3: (0, 255, 255),
    4: (0, 255, 0),
    5: (255, 0, 0),
    6: (255, 0, 255),
}

print(
    """
1->Red
2->Orange
3->Yellow
4->Green
5->Blue
6->Purple
"""
)

color = int(input("Choose the color of light::"))
inc_angle_deg = float(input("Incident angle (degrees)::"))
n1 = float(input("Refractive Index of Upper medium::"))
n2 = float(input("Refractive Index of Lower medium::"))

center = (300, 300)
upper_ref = (300, 0)
lower_ref = (300, 600)
start = time.time()
inc_angle_rad = math.radians(inc_angle_deg)
refract_angle = math.asin((n1 / n2) * math.sin(inc_angle_rad))


def calc_y(angle):
    length = (upper_ref[1] - center[1]) * math.tan(angle)
    return int(length)


incident_ray = (
    upper_ref[0] + int((upper_ref[1] - center[1]) * math.tan(inc_angle_rad)),
    upper_ref[1],
)
refract_ray = (
    lower_ref[0] + int((lower_ref[1] - center[1]) * math.tan(refract_angle)),
    lower_ref[1],
)
reflect_ray = (upper_ref[0] - calc_y(inc_angle_rad), upper_ref[1])

screen = np.zeros((600, 600, 3), dtype=np.uint8)

for x in range(600):
    for y in range(600):
        if x > 300:
            screen[x][y] = [51, 42, 34]

cv.line(screen, (300, 0), (300, 600), (105, 105, 105), 1)
cv.line(screen, (0, 300), (600, 300), (255, 255, 255), 1)
cv.line(screen, center, incident_ray, color_map[color], 1)
cv.line(screen, center, reflect_ray, color_map[color], 1)
cv.line(screen, center, refract_ray, color_map[color], 1)

u_text = f"n1={n1}"
l_text = f"n2={n2}"
r_text = f"{(math.degrees(refract_angle)):.5f}"
i_text = f"{(inc_angle_deg):.5f}"
cv.putText(screen, u_text, (80, 250), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv.putText(screen, l_text, (80, 350), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv.putText(
    screen,
    "Angle of Refraction=",
    (50, 500),
    cv.FONT_HERSHEY_SIMPLEX,
    0.35,
    (255, 255, 255),
    1,
)
cv.putText(screen, r_text, (50, 520), cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
cv.putText(
    screen,
    "Angle of Incidence=",
    (50, 100),
    cv.FONT_HERSHEY_SIMPLEX,
    0.35,
    (255, 255, 255),
    1,
)
cv.putText(
    screen,
    str(inc_angle_deg),
    (50, 120),
    cv.FONT_HERSHEY_SIMPLEX,
    0.35,
    (0, 255, 255),
    1,
)

cv.putText(screen, "X", (590, 290), cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
cv.putText(screen, "-X", (10, 290), cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
cv.putText(screen, "Y", (310, 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
cv.putText(screen, "-Y", (310, 590), cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)

if screen is None:
    raise ValueError("Image not found")

end = time.time()
cv.imshow("Snell's Law Visualizer", screen)
while True:
    if cv.waitKey(1) & 0xFF == 32:
        break
print((end - start))
cv.destroyAllWindows()
