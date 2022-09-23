# Import Libraries
import numpy as np
import cv2 as cv


# Read Webcam

cap = cv.VideoCapture(0)

# Show Camera in Different Shades

while(True):
    (ret, frame) = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # For Gray Shades
    (thresh, binary) = cv.threshold(gray,127,225,cv.THRESH_BINARY) # For Black and White Shades
    cv.imshow('Original', frame) 
    cv.imshow('Gray Shade', gray)
    cv.imshow('Black and White', binary)

    # Quit With q key

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
