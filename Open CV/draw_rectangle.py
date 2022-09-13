import cv2

image = cv2.imread('Open CV\images\image.png')

while True:
    cv2.rectangle(image, (100, 100), (200, 200), (0, 255, 0), 2)
    cv2.imshow('Rectangle', image)
    
    if cv2.waitKey(1) & ord('q'):
        break

cv2.destroyAllWindows()