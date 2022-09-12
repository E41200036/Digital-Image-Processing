# Python program to illustrate
# arithmetic operation of
# addition of two images

import cv2
import numpy as np

image = cv2.imread('Open CV\images\image1.jpg')
image2 = cv2.imread('Open CV\images\image2.jpg')

# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.addWeighted(image, 0.5, image2, 0.4, 0)
cv2.imshow('Weighted Image', weightedSum)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()