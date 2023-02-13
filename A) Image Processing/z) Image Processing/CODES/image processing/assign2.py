import cv2
import numpy as np
img=cv2.imread("abc.jpg")
h=len(img)
w=len(img[0])
c=len(img[0][0])
greyimage=np.zeros([h,w,c])
for i in range(0,h):
    for j in range(0,w):
        t = (int(img[i][j][0])) + (int(img[i][j][1])) + (int(img[i][j][2]))
        greyimage[i][j]=t/3
cv2.imwrite("greyimg.jpg", greyimage)