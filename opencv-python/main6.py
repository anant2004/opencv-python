# corner detection program

import cv2
import numpy as np

gap = cv2.VideoCapture('C:/Users/Anant/Desktop/opencv-python/test_vid3.mp4')

while True:
    ret, frame = gap.read()
    height = int(gap.get(4))
    width = int(gap.get(3))

    if ret:

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

gap.release()
cv2.destroyAllWindows()