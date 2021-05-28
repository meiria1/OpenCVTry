import numpy as np
import cv2 as cv

img = cv.imread('./samples/messi5.jpg',0)
rows, cols = img.shape

# Shift
M = np.float32([[1,0,100], [0,1,50]]) # shift (100,50)
dst = cv.warpAffine(img, M, (cols,rows))


cv.imshow('image',img)
cv.waitKey(0)
cv.imshow('image', dst)
cv.waitKey(0)

# rotate
M = cv.getRotationMatrix2D((cols/2, rows/2),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
print(M)

cv.imshow('image',dst)
cv.waitKey(0)

cv.destroyAllWindows()
