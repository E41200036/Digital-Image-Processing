import cv2
import matplotlib.pyplot as plt

src  = cv2.imread("School Task\images\image.png")
src2 = cv2.imread("School Task\images\image2.png")

# resize image to 512x512
resized_image  = cv2.resize(cv2.cvtColor(src, cv2.COLOR_BGR2GRAY), (512, 512))
resized_image2 = cv2.resize(cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY), (512, 512))

# sum image
sum_image = cv2.add(resized_image, resized_image2)

while True:
    plt.subplot(1, 3, 1)
    plt.imshow(resized_image, cmap="gray")
    plt.title("Image 1")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 3, 2)
    plt.imshow(resized_image2, cmap="gray")
    plt.title("Image 2")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 3, 3)
    plt.imshow(sum_image, cmap="gray")
    plt.title("Sum Image")
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    break