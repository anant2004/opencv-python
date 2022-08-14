import cv2
import random

img = cv2.imread('test.jpg', -1)

#print(img[0])

# img.shape - gives the shape of the image as rows columns and channels

# Ex : (995,1000,3)

# 995 - no. of rows (height of the image)
# 1000 - no. of columns (width of the image)
# 3 - how many values represent each pixel (rgb = 3)

# change pixel colours

#for i in range(200):
#    for j in range(img.shape[1]):
#        img[i][j] = [random.randint(0,255),random.randint(0, 255),random.randint(0, 255)]

# copy and pasting parts of image

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# opencv uses bgr - blue, geen, red
# img in opencv is store as numpy arrays