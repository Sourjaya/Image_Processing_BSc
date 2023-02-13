from PIL import Image
import cv2
import numpy as np
img = cv2.imread("24bitexplosion.jpg")
h = len(img)
w = len(img[0])
c = len(img[0][0])
grayimage=np.empty([h,w],'uint8')
for i in range(0,h):
    for j in range(0,w):
        grayimage[i][j]=0.114*img[i][j][0]+0.587*img[i][j][1]+0.299*img[i][j][2]
cv2.imshow('grayimage',grayimage)
cv2.waitKey(5000)
cv2.imwrite('grayimg.jpeg',grayimage)
