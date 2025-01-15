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

![Incident Ray Calculation](img1x01.svg)

The formula used is:

\[
\tan(\theta) = \frac{x}{URP[1] - CP[1]}
\]

Next, the code applies Snell's Law to calculate the angle of refraction and draw the refracted ray:

\[
n_1 \sin(\text{Angle of incidence}) = n_2 \sin(\text{Angle of refraction})
\]

> **Note:** The project isn't completed yet. Real-world phenomena like total internal reflection, critical angle cases, etc., are still to be implemented.

