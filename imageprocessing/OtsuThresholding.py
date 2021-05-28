import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./samples/noisy 2.png',0)

ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

blur = cv.GaussianBlur(img,(5,5),0)

ret3, th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)

images = [img, 0, th1,
        img, 0, th2, 
        blur, 0, th3]
titles = ['Original noisy image', 'Histogram', 'Global threhsholding',
        ' Original noisy image', 'Histogram', 'Otsus thresholding',
        'Gaussian filtered image','Histogram','Otsus thresholding']


for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()