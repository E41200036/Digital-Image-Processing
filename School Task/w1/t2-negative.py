import cv2
import matplotlib.pyplot as plt

src            = cv2.imread("School Task\images\image.png")
gray_image     = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
negative_image = cv2.bitwise_not(gray_image)

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
    plt.imshow(negative_image, cmap="gray")
    plt.title("Negative")
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    break




