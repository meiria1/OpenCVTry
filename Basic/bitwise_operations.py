import numpy as np
import cv2 as cv

img1 = cv.imread('./samples/messi5.jpg')
img2 = cv.imread('./samples/opencv-logo-white.png')

# create an roi to put the logo on the top left corner
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# create a mask of the logo and the inverse of the mask as well
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# black out the logo area in the image
img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)

# take only the region of logo from logo image
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
