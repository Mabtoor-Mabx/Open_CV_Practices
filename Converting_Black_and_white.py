# Import Libraries

import numpy as np
import cv2 as cv 

# Reading Images

img = cv.imread('Resources/image.jpg')
resize_image = cv.resize(img, (800,600))

# Converting in GreyScale

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Convert in Black and White

(thresh, binary) = cv.threshold(grey, 127,255, cv.THRESH_BINARY)

# Displaying All Images

cv.imshow('ORIGINAL Image', img)
cv.imshow('Resize Image', resize_image)
cv.imshow('Gray Image', grey)
cv.imshow('Black and White Image', binary)

# Saving The Images
cv.imwrite('Resources/grey_image.jpg', grey)
cv.imwrite('Resources/resize_image.jpg', resize_image)
cv.imwrite('Resources/black_and_white.jpg', binary)

# Stilling The Images

cv.waitKey(0)
cv.destroyAllWindows()








