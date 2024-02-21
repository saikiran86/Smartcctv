import cv2
import numpy as np
from datetime import datetime

def record():
    cap = cv2.VideoCapture(0)

    # Initialize variables for motion detection
    prev_frame = None
    motion_threshold = 500  # Adjust this value based on your requirements

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None  # VideoWriter object for recording
    is_recording = False  # Flag to indicate if recording is active
    pause_duration = 0  # Counter to track the duration of the pause

    while True:
        _, frame = cap.read()

        # Convert frame to grayscale for motion detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # remove noise
        gray = cv2.GaussianBlur(gray, (21, 21), 0) #value from google

        # Perform motion detection by calculating frame difference
        if prev_frame is None:
            prev_frame = gray
            continue

        frame_delta = cv2.absdiff(prev_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) > motion_threshold:
                motion_detected = True
                break

        # Update previous frame
        prev_frame = gray

        if motion_detected:
            if not is_recording:
                # Start recording or resume recording
                is_recording = True
                out = cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi',
                                      fourcc, 20.0, (640, 480))
                pause_duration = 0  # Reset pause duration when starting or resuming recording
        else:
            if is_recording:
                # Increment pause duration
                pause_duration += 1

                if pause_duration >= 100:  # Pause duration of 100 frames (5 seconds) before stopping recording
                    # Stop recording
                    is_recording = False
                    out.release()
                    prev_frame = None  # Reset previous frame when resuming recording

        if is_recording:
            cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (255, 255, 255), 2)
            out.write(frame)

        cv2.imshow("esc. to stop", frame)

        if cv2.waitKey(1) == 27:
            if is_recording:
                out.release()
            cap.release()
            cv2.destroyAllWindows()
            break
