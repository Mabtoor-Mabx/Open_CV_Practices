# Import Libraries
import numpy as np
import cv2 as cv  

# Reading Video

cap = cv.VideoCapture('Resources/video.mp4')

# Converting Video in Grey Format

while(True):
    (ret, frame) = cap.read()
    greyframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if(ret)==True:
        cv.imshow('Video', greyframe)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
cv.destroyAllWindows()

