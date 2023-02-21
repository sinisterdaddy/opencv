import numpy as np
import cv2 as cv

blank = np.zeros((500,500,3), dtype ="uint8")
cv.imshow("blank",blank)
#blank[:] = 0,255,0   #for red 0,0,255    for blue 255,0,0
#cv.imshow("green", blank)
#paint the image a certain color
#blank[200:300 , 300:400] = 0,0,255   # can color particular portion of image
#cv.imshow("red", blank)
#img = cv.imread("photos/dog.jpg")
#cv.imshow("dog", img)

cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2)  
# to fill the imagae can write thickness=-1 or cv.filled 
# also instead of  scalling can also write (blank.shape[1]//2,blank.shape[0]//2)
cv.imshow("rectangle", blank)

#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 50,(0,0,255), thickness = 2 )
cv.imshow("circle" , blank)

cv.line(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255), thickness = 2)
cv.imshow("line" , blank)

cv.putText(blank , "hii my name is rk", (225,225) , cv.FONT_HERSHEY_COMPLEX, 0.75 , 
(255,255,0), thickness=2 )
cv.imshow("text" , blank)
cv.waitKey(0)