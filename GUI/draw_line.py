import numpy as np
import cv2 as cv

def draw_image(img):
    while True:
        cv.imshow("image",img)
        if cv.waitKey(1) == ord("q"):
            break

img = np.zeros((512,512,3),np.uint8)

cv.line(img, (0,0), (511,511), (255,0,0), 5)
draw_image(img)

cv.rectangle(img, (384,0), (510,128), (0,255,0),3)
draw_image(img)

cv.circle(img, (447,63), 63, (0,0,255),1)
draw_image(img)

cv.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)
draw_image(img)

font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, "OPENCV", (10,500), font, 4, (255,255,255), 2, cv.LINE_AA)
draw_image(img)



