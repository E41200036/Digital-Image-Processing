import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread('School Task\images\image.png')
image2 = cv2.imread('School Task\images\image2.jpg')

image2_cvt = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
image3     = image1 + image2_cvt

while True:
    plt.subplot(1, 3, 1)
    plt.imshow(image1)
    plt.title('Image 1')

    plt.subplot(1, 3, 2)
    plt.imshow(image2)
    plt.title('Image 2')

    plt.subplot(1, 3, 3)
    plt.imshow(image3)
    plt.title('Image 3')

    plt.show()
