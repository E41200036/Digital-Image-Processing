from email.mime import image
import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread('Open CV\images\image.png')

# convert image -> gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
print(gray.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

# convert image -> rgb
# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)