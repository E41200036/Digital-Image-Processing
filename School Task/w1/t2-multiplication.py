import cv2
import matplotlib.pyplot as plt

originalImage = cv2.imread('School Task\images\image.png')
image = originalImage * 2

while True:
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Multiplied by 2')
    plt.xticks([]), plt.yticks([])

    plt.show()
    break
