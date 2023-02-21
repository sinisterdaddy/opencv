import cv2 as cv

#reading images
img =  cv.imread("photos/dog.jpg")
cv.imshow("dog", img)

cv.waitKey(0) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding

