from email.mime import image
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("School Task\images\image.png")

rgb_image  = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

while True:
    plt.subplot(1, 2, 1)
    plt.imshow(rgb_image)
    plt.title("Citra Asli")

    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Citra Grayscale")
    
    plt.show()