import cv2
gray = cv2.imread("abc.jpg",0)
cv2.imwrite("gray.jpg", gray)