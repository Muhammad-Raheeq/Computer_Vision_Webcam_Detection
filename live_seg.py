import cv2
from ultralytics import YOLO

def main():
    model = YOLO("yolo11n-seg.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Starting webcam... Press 'q' on the video window to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to receive frame from webcam.")
            break

        results = model(frame, stream=True, verbose=False)

        for result in results:
            annotated_frame = result.plot()

            cv2.imshow("YOLO Live Segmentation", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()