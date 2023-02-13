import cv2
import numpy as np
gray = cv2.imread("abc.jpg",0)
cv2.imwrite("gray.jpg", gray)
gray=np.array(gray)
i=int(input("i="))
j=int(input("j="))
print(gray[i][j])
