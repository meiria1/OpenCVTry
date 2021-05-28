import numpy as np
import cv2 as cv
from os import walk
import time
import fnmatch
import math

MAX_IMAGE_SIZE = 600
def blend_images(img1, img2, w):
    width = img1.shape[0]
    height = img1.shape[1]

    if height>MAX_IMAGE_SIZE:
        aspect_ratio = width/height
        height = MAX_IMAGE_SIZE
        width = round(MAX_IMAGE_SIZE*aspect_ratio)
        dim = (height, width)
        img1 = cv.resize(img1,dim)
    dim = (height, width)
    img2 = cv.resize(img2, dim)
    blend_image = cv.addWeighted(img1,1-w,img2,w,0)
    return blend_image


mypath='./samples/'
f = []
print('------------------')
for (dirpath, dirnames, filenames) in walk(mypath):
    for name in filenames:
        if name.endswith('.png'):
            f.append(name)
print('------------------')
print(f)
print('++++++++++++++++')

first_image=True
for filename in f:
    print(mypath + filename)
    if first_image==True:
        first_image = False
        curr_image = cv.imread(mypath + filename)
        blend_image=curr_image
    else:
        prev_image = curr_image
        curr_image = cv.imread(mypath + filename)
        for w in range(100):
            blended_image = blend_images(prev_image,curr_image,w/100)
            cv.imshow('image',blended_image)
            k = cv.waitKey(50)
            if k==27:
                break
        
       


    

cv.destroyAllWindows()


