# drawing lines, images, circles, text 

import cv2
import numpy as np

cap = cv2.VideoCapture('C:/Users/Anant/Desktop/opencv-python/test_vid2.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # drawing lines

    # cv2.line(src_img, starting_point(tuple), ending_point(tuple), colour(bgr), line thickness(px))
    img = cv2.line(frame, (0,0), (width,height), (0,255,0), 6)
    img = cv2.line(img, (width,0), (0,height), (0,0,255), 6)

    # drawing rectangle

    # cv2.rectangle(src_img, top_left_corner, bottom_right_corner, colour(bgr), thickness(px), -1-for filling the shape)
    cv2.rectangle(img, (100,100), (300,200), (255,0,0), 2)

    # drawing circles

    # cv2.circle(src_img, center_of_circle, radius, colour, thickness)

    cv2.circle(img, (300,300), 60, (0,2550,0), 5)

    # drawing text

    font  = cv2.FONT_HERSHEY_DUPLEX     # declaring the font type
    # cv2.putText(scr_img, 'text_to_display', bottom_left_position, font, scale, colour, thickness, line_type))
    img  = cv2.putText(img, 'Anant', (200,height-10), font, 4,(0,0,0), 3, cv2.LINE_AA)
    
    if ret:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()