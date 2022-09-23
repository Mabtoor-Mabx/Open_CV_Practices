# Import Libraries
import numpy as np
import cv2 as cv 

# Read Video

cap = cv.VideoCapture('Resources/video.mp4')

# Indicator 

if(cap.isOpened()==False):
    print('Error in Uploading Video')

# Saving Video using OPEN_CV

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('Resources/output_video.avi', cv.VideoWriter_fourcc('M','J','P','G'), 9, (frame_width, frame_height))

# Playing Video Frame By Frame

while(True):
    (ret, frame) = cap.read()
    greyframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if(ret)==True:
        out.write(frame)
        cv.imshow('Video', greyframe)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv.destroyAllWindows()