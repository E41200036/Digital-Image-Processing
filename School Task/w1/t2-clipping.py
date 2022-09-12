import cv2
import matplotlib.pyplot as plt

src = cv2.imread("School Task\images\image.png")

# convert to grayscale
gray_image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# clipping image
clipped_image = cv2.bitwise_and(gray_image, 100)

while True:
    plt.subplot(1, 3, 1)
    plt.imshow(src)
    plt.title("Original")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Gray")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 3, 3)
    plt.imshow(clipped_image, cmap="gray")
    plt.title("Clipped")
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    break