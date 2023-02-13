import cv2
import numpy as np
img=cv2.imread("image2.jpg",0)
cv2.imshow('image',img)

h = len(img)
w = len(img[0])

arr=np.zeros([h,w,8],dtype='uint8')
for i in range(0,h):
    for j in range(0,w):
        for k in range(0,7):
            arr[i][j][7-k]=(img[i][j]%2)*255
            img[i][j]=img[i][j]/2
        
arr2=np.zeros([h,w],dtype='uint8')
for i in range(0,7):
    str1='img'+str(i)
    for j in range(0,h):
        for k in range(0,w):
            arr2[j][k]=arr[j][k][i]

    cv2.imshow(str1,arr2)
    cv2.waitKey(5000)


