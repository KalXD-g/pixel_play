import cv2 as cv
import numpy as np

# Video path
video_path = "sample_2.avi"

cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Background subtractor with shadow detection disabled
object_detector = cv.createBackgroundSubtractorMOG2(
    history=100, varThreshold=40, detectShadows=False)

# Kernel for morphological operations
morph_kernel = np.ones((3, 3), np.uint8)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Reached the end of the video.")
        break

    # Define the region of interest (hardcoded ROI)
    interest_region = frame[96:460, 0:]

    # Convert the ROI to grayscale
    gray_frame = cv.cvtColor(interest_region, cv.COLOR_BGR2GRAY)

    # Apply the background subtractor
    mask = object_detector.apply(gray_frame)

    # Perform morphological opening (erosion + dilation) to clean the mask
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, morph_kernel)

    # Apply a high threshold to remove shadows and keep only strong foreground objects
    _, mask = cv.threshold(mask, 254, 255, cv.THRESH_BINARY)

    # Find contours on the binary mask
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Process the contours
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:  # Filter small contours
            # Get the bounding rectangle for the contour
            x, y, w, h = cv.boundingRect(cnt)

            # Draw the bounding rectangle on the ROI
            cv.rectangle(interest_region, (x, y),
                         (x + w, y + h), (0, 255, 0), 2)

    # Display the processed ROI
    cv.imshow('Video Player', interest_region)

    # Break the loop if 'q' is pressed
    if cv.waitKey(40) & 0xFF == ord('q'):
        print("Video stopped by user.")
        break

# Release resources
cap.release()
cv.destroyAllWindows()