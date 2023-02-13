import cv2
import os
import uuid
import time


def CaptureImages(Labels: list, NumberOfImages: int, Directory: str):
    cap = cv2.VideoCapture(0)
    for Class in Labels:
        print(f"Collecting Images for {Class} in 5 Seconds...")
        for idx in range(NumberOfImages):
            _, img = cap.read()
            print(
                f"Collecting Image name {os.path.join(Directory,Class,str(uuid.uuid1()))}.jpg"
            )
            cv2.imshow("Display", img)
            cv2.imwrite(os.path.join(Directory, Class, str(uuid.uuid1())) + ".jpg", img)
            time.sleep(2)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break


ImageClasses = ["ThumbsUp", "ThumbsDown", "LiveLong", "Unknown"]
DirPath = "C:\Computer Vision Projects\TFObjectDetection\Dataset"
CaptureImages(ImageClasses, 5, DirPath)
