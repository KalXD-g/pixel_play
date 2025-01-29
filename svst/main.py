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


def is_inside(rect1, rect2):
    # Check if rect1 is completely inside rect2.
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return x1 > x2 and y1 > y2 and (x1 + w1) < (x2 + w2) and (y1 + h1) < (y2 + h2)


def is_overlapping(rect1, rect2):
    # Check if rect1 and rect2 overlap
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Reached the end of the video.")
        break

    # Define the region of interest (hardcoded ROI)
    interest_region = frame[96:460, 0:]

    interest_region = cv.GaussianBlur(interest_region, (5, 5), 0)

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

    # Store bounding rectangles
    rectangles = [cv.boundingRect(cnt)
                  for cnt in contours if cv.contourArea(cnt) > 100]

    # Sort rectangles by area (largest first)
    rectangles.sort(key=lambda r: r[2] * r[3], reverse=True)

    # Filter out smaller rectangles if they overlap or are inside another
    filtered_rectangles = []
    for i, rect1 in enumerate(rectangles):
        keep = True
        for j, rect2 in enumerate(filtered_rectangles):
            if is_inside(rect1, rect2) or is_overlapping(rect1, rect2):
                keep = False
                break
        if keep:
            filtered_rectangles.append(rect1)

    # Draw the filtered bounding rectangles
    for x, y, w, h in filtered_rectangles:
        cv.rectangle(interest_region, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed ROI
    cv.imshow('Video Player', interest_region)

    # Break the loop if 'q' is pressed
    if cv.waitKey(40) & 0xFF == ord('q'):
        print("Video stopped by user.")
        break

# Release resources
cap.release()
cv.destroyAllWindows()
