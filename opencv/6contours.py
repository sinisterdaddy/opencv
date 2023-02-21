# contours are basically boundaries of the object the line or curve that join boundaries countours and edge are diff rent
#after reading convert to grayscale
#catch edges using canny
#countours using find countours method this returns countours and heirachies and takes in canny and moded to find the countours
#looks at edges and returns the coutours
# using bur image for countours will reduce them
# thresholding ---> binarising the image if intensity below 125 reduces it to 0 and above takes it 255
#cv.drawContours(blank, contours, -1, (0,0,255), 1)  to draw contours on blank image we used -1 fo all of them
# found edges of image and drwan them
# using canny gets more thinner and better 

import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
cv.imshow('dog', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)