#we smooth image when it has lot of noise because of camera sensors and all 
#blur is applied to middle pixels as a result of pixels around it
#averaging ---> avg of sourronding applied to middle[given to that region]
import cv2 as cv

img = cv.imread('photos/ironman.jpg')
cv.imshow('ironman', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)   #higher the kernel size more the blur
#more natural to averaging ,  intead of avg each each soornding element is given a weigh the avg of prdcts of those weights gives us
#blurr
cv.imshow('Gaussian Blur', gauss)

# Median Blur   
#same as avg instead of finding avg finds median of sourrding elements
#not meant for high kernel sizes
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
#used in more advanced old methods dont take care of images but it
# retains the edges
bilateral = cv.bilateralFilter(img, 10, 35, 25) #img , diameter , sigmacolor--> means more colors will be considerd in neighbourhood
#when blue is computed , sigmaspace---> means pixels further out will affect blurring calculations 

cv.imshow('Bilateral', bilateral)

cv.waitKey(0)