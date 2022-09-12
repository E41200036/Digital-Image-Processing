from ctypes import resize
import cv2
import matplotlib.pyplot as plt

image  = cv2.imread("School Task\images\image.png")
image2 = cv2.imread("School Task\images\logo.png")

# resize image to 512x512
resize_image  = cv2.resize(image, (512, 512))
resize_image2 = cv2.resize(image2, (512, 512))

# convert to grayscale
gray_image  = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(resize_image2, cv2.COLOR_BGR2GRAY)

# substract image
result_image = cv2.subtract(gray_image, gray_image2)

while True:
    plt.subplot(1, 3, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Image 1")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 3, 2)
    plt.imshow(gray_image2, cmap='gray')
    plt.title("Image 2")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 3, 3)
    plt.imshow(result_image, cmap='gray')
    plt.title("Result Image")
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    break