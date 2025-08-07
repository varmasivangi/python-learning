import cv2  as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

image = cv.imread('openCV2/media/profile.jpeg', -1)

# cv.imshow('image', image)
blank[:] = (0, 255, 0)
cv.imshow('blank', blank)
cv.waitKey(0)
cv.destroyAllWindows()