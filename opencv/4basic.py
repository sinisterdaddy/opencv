from tkinter import CASCADE
import cv2 as cv
img =  cv.imread("photos/dog.jpg")
cv.imshow("dog", img)

#converting to grayscale
gray=cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)  #kernel size need to be odd increasing it will blur image more
cv.imshow("blur", blur)

#edge cascade
canny = cv.Canny(img,125,175)
cv.imshow("canny", canny)

canny = cv.Canny(blur,125,175)
cv.imshow("canny2", canny)   #by this we can reduce the no. of edges found.

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)   # will resize it to 500,500 irspective of the aspect ratio

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)  

cv.waitKey(0) 