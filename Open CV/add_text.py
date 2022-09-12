from cgitb import text
from email.mime import image
import numpy as np
import cv2

image = cv2.imread('Open CV\images\image.png')
output = image.copy()

text = "Open CV"
cv2.putText(output, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

while True:
    cv2.imshow("Text", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
