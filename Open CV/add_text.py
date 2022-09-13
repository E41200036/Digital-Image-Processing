import cv2
import matplotlib.pyplot as plt

src_image = cv2.imread("Open CV\images\image.png")

# convert image to rgb color
rgb_image  = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

while True:
    plt.subplot(1,3,1)
    plt.imshow(rgb_image)
    plt.title("RGB Image")

    plt.subplot(1,3,2)
    plt.imshow(src_image)
    plt.title("BGR Image")

    plt.subplot(1,3,3)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Gray Image")
    
    plt.show()
    break
