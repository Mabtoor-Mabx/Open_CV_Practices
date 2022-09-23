import imghdr
import numpy as np
import cv2 as cv

# For Reading The Images

img = cv.imread('Resources/\Mabtoor Mabx-2.png')

# For Displaying The Images

cv.imshow('First Image', img)

cv.waitKey(0)
cv.destroyAllWindows()