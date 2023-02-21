#RADHA KRISHNA GARG COMPUTER VISION PROJECT
from asyncore import read
import cv2 as cv

#reading images
img =  cv.imread("photos/dog.jpg")
cv.imshow("dog", img)

cv.waitKey(0) 

#reading videos

capture = cv.VideoCapture("videos/catvid1.mp4")
while True:
    isTrue , frame = capture.read()
    cv.imshow("cat",frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release
cv.destroyAllWindows



