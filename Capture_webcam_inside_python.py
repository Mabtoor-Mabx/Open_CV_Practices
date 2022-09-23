# Import Libraries
import numpy as np
import cv2 as cv

# Open Laptop Camera

cap = cv.VideoCapture(0) # 1 for Webcam

# Read Until the End

while(cap.isOpened()):
    # Capture Frame by Frame
    ret, frame = cap.read()
    if ret == True:
        # To Display Frame
        cv.imshow('Frame', frame)

        # To Quit with Key
        if cv.waitKey(1) &  0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()