import cv2
import matplotlib.pyplot as plt

img  = cv2.imread('School Task\images\image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img  = img / 2

while True:
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.imshow(img, cmap='gray')
    plt.title('Divided by 2')
    plt.xticks([]), plt.yticks([])

    plt.show()
    break
