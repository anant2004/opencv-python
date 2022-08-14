import cv2

img = cv2.imread('test.jpg', -1)

# 0 - for greyscale
# -1 - for normal coloured image
# 1 - to ingrore the alpha values(transperency)

# resizing an image

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# fx and fy can be used to resize the image in a specific manner if fx = 0.5 and fy = 0.5 then the image will become half of its original resolution

# rotationg an image

img = cv2.rotate(img, cv2.ROTATE_180)

# cv2.ROTATE_90_CLOCKWISE - to rotate the image clockwise
# cv2.ROTATE_90_COUNTERCLOCKWISE - to rotate the image counterclockwise
# cv2.ROTATE_180 - to rotate the image 180

# saving the image as a new image

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)          # to wait an infinite amount of time before closing
cv2.destroyAllWindows()         # close the window whwn any key is pressed