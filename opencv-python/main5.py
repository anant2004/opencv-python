# colour detection program

import cv2
import numpy as np

cap = cv2.VideoCapture('C:/Users/Anant/Desktop/opencv-python/test_vid3.mp4')

while True:

    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)        # to convert bgr to hsv(hue,saturation,brightness)
    lower_blue = np.array([90,50,50])           # lower blue colour detection range
    upper_blue = np.array([130,255,255])        # upper blue colour detection range

    mask = cv2.inRange(hsv, lower_blue, upper_blue)         # mask to filter the blue parts

    result = cv2.bitwise_and(frame, frame, mask=mask)       # comparision of the frames with and without the mask
    smaller_frame = cv2.resize(result, (0,0), fx=0.5, fy=0.5)       # reducing the aspect ratio

    if ret:
        cv2.imshow('Frame', smaller_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()