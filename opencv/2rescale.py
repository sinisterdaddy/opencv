
from configparser import Interpolation
from tkinter import Frame, Scale
import cv2 as cv

def rescaleframe(frame, scale=0.2):
    width= int(frame.shape[1] * scale)

    height= int(frame.shape[0] * scale)

    dimension=(width,height)

    return  cv.resize(frame,dimension, interpolation=cv.INTER_AREA)
capture = cv.VideoCapture("videos/catvid1.mp4")
while True:
    isTrue , frame = capture.read()
    frame_resized= rescaleframe(frame, scale=0.75)


    if cv.waitKey(20) & 0xFF==ord("d"):
        break
    cv.imshow("catvid1" , frame)
    cv.imshow("resized image", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release
cv.destroyAllWindows

