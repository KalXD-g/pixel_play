# Snell's Law Visualizer

> The name defines the project.

## List of Dependencies
1. Python 3.12.3
2. OpenCV
3. Python Math Library
4. NumPy Library
5. Time Module (Optional)

## Functionality
The code takes the following inputs from the user:
- Angle of incidence
- Refractive index of the 1st medium
- Refractive index of the 2nd medium
- The color of light

## How It Works
The code creates a black image of size 600x600 pixels, with the center point set at (300, 300). This is where the media separator and normal intersect.

With the angle of incidence provided by the user, the code calculates the distance between the normal line and the reference point needed to draw the incident ray.

![Incident Ray Calculation](https://github.com/zenwing-g/pixel_play/blob/main/snell/.assets/img1x01.png)

The formula used is:

![Formula for calculating Y](https://github.com/zenwing-g/pixel_play/blob/main/snell/.assets/img1x02.jpg)

Next, the code applies Snell's Law to calculate the angle of refraction and draw the refracted ray:

![Snell's Law](https://github.com/zenwing-g/pixel_play/blob/main/snell/.assets/img1x03.jpg)

> **Note:** The project isn't completed yet. Real-world phenomena like total internal reflection, critical angle cases, etc., are still to be implemented.

