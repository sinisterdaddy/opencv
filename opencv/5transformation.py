#will take list with 2 list inside it
#created a matrix

import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
cv.imshow('dog', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)   #-ve clockwise +ve anticlockwise
cv.imshow('Rotated', rotated) #instead of directly -90 to get vertical image if rotate the already roataed -45 deg image again by -45 deg
# we wont get vertical image as the already roated image cointains black background triangles which will also rotate along resulting in 
# a skewed type image

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)    # use 0 for vertical flipping , 1 for horizontal , -1 for both
cv.imshow('Flip', flip)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped) 

cv.waitKey(0)