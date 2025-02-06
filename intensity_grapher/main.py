import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# bbit.py code integrated into grp.py
def get_intensities(image):
    if image is None:
        raise ValueError("Error: Unable to load image. Check the file path.")

    tb = np.sum(image[:, :, 0])  # Blue channel sum
    tg = np.sum(image[:, :, 1])  # Green channel sum
    tr = np.sum(image[:, :, 2])  # Red channel sum
    ti = tb + tg + tr  # Total intensity

    if ti == 0:
        return [0, 0, 0]  # Avoid division by zero if total intensity is zero

    # Calculate intensity percentages for each channel
    bi = (tb / ti) * 100  # Blue intensity percentage
    gi = (tg / ti) * 100  # Green intensity percentage
    ri = (tr / ti) * 100  # Red intensity percentage

    return [bi, gi, ri]


# Main processing code from grp.py
video_path = input("Video Path:")
cap = cv.VideoCapture(video_path)

# Get total number of frames in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
print(f"Total frames in the video: {total_frames}")

red_line = []
blue_line = []
green_line = []

# Process each frame of the video
while True:
    ret, frame = cap.read()

    if not ret:
        print("No further frame found")
        break

    # Get the intensities for each frame
    intensities = get_intensities(frame)
    red_line.append(intensities[2])
    blue_line.append(intensities[0])
    green_line.append(intensities[1])

cap.release()
cv.destroyAllWindows()

# Plotting with a black background and no legend
plt.style.use('dark_background')

# Plotting the intensities for each color channel
plt.plot(red_line, color='red')
plt.plot(blue_line, color='blue')
plt.plot(green_line, color='green')

plt.xlabel('Frame Number')
plt.ylabel('Intensity')
plt.title('Color Intensity Over Time')

plt.show()

# Verify that the sum of intensities for each frame is close to 100
tots = []
for i in range(len(red_line)):
    tots.append(red_line[i] + green_line[i] + blue_line[i])

# Print the sums for verification
for p in tots:
    print(int(p), end = ", ")
