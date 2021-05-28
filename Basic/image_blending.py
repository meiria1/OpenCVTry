import numpy as np
import cv2 as cv

img1 = cv.imread('./samples/ml.png')
img2 = cv.imread('./samples/opencv-logo.png')
img2 = img2[0:380,0:308]

print(img2.shape)

dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()