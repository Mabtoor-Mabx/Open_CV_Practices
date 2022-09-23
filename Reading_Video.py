#Import Libraries
import numpy as np
import cv2 as cv  


# Reading Video

cap= cv.VideoCapture('Resources/video.mp4')

# Indicator
if(cap.isOpened()==False):
    print('Error in Reading Video')
    # Reading and Playing
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Video', frame)
        # Quiting for Q Key 
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()

