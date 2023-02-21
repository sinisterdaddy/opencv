#pylint:disable=no-member

import cv2 as cv
#import matplotlib.pyplot as plt

img = cv.imread('photos/supra.jpg')
cv.imshow('supra', img)

# plt.imshow(img)     
# plt.show()
# opencv displays bgr images but matplot lib doesnt so displays as RGB hence we see inversion of color

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # hue saturation value based upon how humans see and think abt colors

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)    
#cant covert grayscale to HSV if we want grayscale --> BGR ---> HSV 

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)