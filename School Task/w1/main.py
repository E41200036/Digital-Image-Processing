from colorsys import rgb_to_yiq
import cv2
import numpy as np
import matplotlib.pyplot as plt

image          = cv2.imread('School Task\images\image.png')
rgb_image      = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image     = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

negative_image = 255 - image
clip_image     = np.clip(image, 0, 159)

while True:

    plt.subplot(2, 2, 1)
    plt.imshow(rgb_image)
    plt.title('RGB Image')

    plt.subplot(2, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Gray Image')

    plt.subplot(2, 2, 3)
    plt.imshow(negative_image)
    plt.title('Negative Image')

    plt.subplot(2, 2, 4)
    plt.imshow(clip_image)
    plt.title('Clip Image')

    plt.show()
    break
