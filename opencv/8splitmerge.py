#allows to split an image into its blue,green and red componeents
#we can visualize the shape of the image 
#after running we get diff type of image we get grayscale images
#region where its lighter depcits more color a that part
#shape the component is 1 we dont see it when printed but we get grayscale images which have shape=1
#
import cv2 as cv
import numpy as np

img = cv.imread('photos/ironman.jpg')
cv.imshow('ironman', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)