import cv2 as cv
from ultralytics import YOLO

# Load YOLO model
model = YOLO("YOLO_models/yolov8n.pt")

# Load video
cap = cv.VideoCapture("sample_2.avi")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on the frame
    results = model(frame)[0]  # Get detection results

    for box in results.boxes.data:  # Iterate over detections
        x1, y1, x2, y2, conf, cls = box.tolist()
        cls = int(cls)  # Convert class ID to integer

        if cls == 0:
            # Draw bounding box
            cv.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Display the output
    cv.imshow("Human Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()