import cv2
import numpy as np
img=cv2.imread("abc.png")
h=len(img)
w=len(img[0])
c=len(img[0][0])
grimage=np.zeros([h,w])
ggimage=np.zeros([h,w])
gbimage=np.zeros([h,w])
for i in range(0,h):
    for j in range(0,w):
        gbimage[i][j]=img[i][j][0]
        ggimage[i][j]=img[i][j][1]
        grimage[i][j]=img[i][j][2]
cv2.imwrite("gbimg.jpg", gbimage)
cv2.imwrite("ggimg.jpg", ggimage)
cv2.imwrite("grimg.jpg", grimage)
cv2.imshow('gb.jpg',gbimage)
cv2.imshow('gg.jpg',ggimage)
cv2.imshow('gr.jpg',grimage)

