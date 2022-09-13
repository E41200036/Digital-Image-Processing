import cv2
import matplotlib.pyplot as plt

image  = cv2.imread('School Task\images\image.png')
image2 = cv2.imread('School Task\images\image2.png')

result = cv2.bitwise_or(cv2.resize(image, (512, 512)), cv2.resize(image2, (512, 512)))

while True:
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Image 1')
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    plt.title('Image 2')
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title('Result')
    plt.xticks([]), plt.yticks([])

    plt.show()
    break