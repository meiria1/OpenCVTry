import numpy as np
import cv2 as cv

img = cv.imread('./samples/messi5.jpg')
cv.imshow('image', img)
print('image shape: ',img.shape)
print('image size: ', img.size)
print('data type: ', img.dtype)

# image roi
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if (k==27):
        break

# splitting and merging image channels
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

while(1):
    cv.imshow('image',g)
    k = cv.waitKey(1) & 0xFF
    if (k==27):
        break

img_border = cv.copyMakeBorder(img, 10,20,10,20,cv.BORDER_CONSTANT,value=[255, 0, 0])
while(1):
    cv.imshow('image',img_border)
    k = cv.waitKey(1) & 0xFF
    if (k==27):
        break