from email.mime import image
import cv2

image = cv2.imread("Open CV\images\image.png")
h, w = image.shape[:2]
print("Height: {}, Width: {}".format(h, w))