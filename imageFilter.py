import cv2

img = cv2.imread('Img_2.png')

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

