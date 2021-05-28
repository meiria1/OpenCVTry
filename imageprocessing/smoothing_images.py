import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('./samples/opencv-logo.png')

kernel = np.ones((5,5), np.float32)/25
# dst = cv.filter2D(img,-1,kernel)
dst = cv.blur(img,(5,5))
dst = cv.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

