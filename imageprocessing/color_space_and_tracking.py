import numpy as np
import cv2 as cv

blue=np.uint8([[[0, 0, 255]]])
hsv_blue = cv.cvtColor(blue,cv.COLOR_BGR2HSV)
print ('------------------------')
print(hsv_blue)
print ('------------------------')

cap = cv.VideoCapture(0)



while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv.inRange(hsv,lower_blue,upper_blue)

    res = cv.bitwise_and(frame,frame,mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    k=cv.waitKey(5) & 0xFF
    if k==27:
        break

cv.destroyAllWindows()
