import cv2
from datetime import datetime
import os

def in_out():
    cap = cv2.VideoCapture(0)
    right, left = False, False

    # Create the visitors directory if it doesn't exist
    visitors_dir = "visitors"
    if not os.path.exists(visitors_dir):
        os.makedirs(visitors_dir)

    in_dir = os.path.join(visitors_dir, "in")
    out_dir = os.path.join(visitors_dir, "out")

    # Create the "in" and "out" subdirectories if they don't exist
    if not os.path.exists(in_dir):
        os.makedirs(in_dir)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    while True:
        _, frame1 = cap.read()
        frame1 = cv2.flip(frame1, 1)
        _, frame2 = cap.read()
        frame2 = cv2.flip(frame2, 1)

        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.blur(diff, (5, 5))
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
        contr, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        x = 300
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

        if not right and x > 500:
            print("to left")
            right = True
            left = False
            file_name = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg"
            file_path = os.path.join(in_dir, file_name)
            cv2.imwrite(file_path, frame1)
            print("Image captured:", file_path)
        elif not left and x < 200:
            print("to right")
            right = False
            left = True
            file_name = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg"
            file_path = os.path.join(out_dir, file_name)
            cv2.imwrite(file_path, frame1)
            print("Image captured:", file_path)

        cv2.imshow("", frame1)
        k = cv2.waitKey(1)

        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
