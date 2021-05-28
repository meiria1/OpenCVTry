import numpy as np
import cv2 as cv

img = cv.imread('./Samples/messi5.jpg')
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# better single pixel accesing method
print(img.item(10, 10, 2))

img.itemset((10,10,2),100)
print(img.item(10,10,2))
print(img [10, 10, 2])
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k==27:
        break