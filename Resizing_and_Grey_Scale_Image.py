# Import Libraries
import numpy as np
import cv2 as cv 

# Reading Images

img = cv.imread('Resources/Mabtoor Mabx-2.png')


# Resizing The Images

img2 = cv.resize(img,(800,600))

# Convert The Image into Grey Scale

img3 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Displaying The Images

cv.imshow('First Image', img)
cv.imshow('Second Image', img2)
cv.imshow('Third Image', img3)

# For Still Existing the image

cv.waitKey(0)
cv.destroyAllWindows()


