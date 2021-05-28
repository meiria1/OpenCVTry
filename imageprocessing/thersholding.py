import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./samples/gradient.png',0)
res, thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
res, thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
res, thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
res, thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
res, thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Origianl Image', 'binary', 'binary inv', 'trunc', 'ToZero',' tozero_inv']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


