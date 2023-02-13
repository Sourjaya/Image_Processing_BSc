import cv2
import numpy as np
img=cv2.imread("image2.jpg",0)
cv2.imshow('image',img)

h = len(img)
w = len(img[0])
k=0
arr1=np.zeros([h,w],dtype='uint8')
arr2=np.zeros([h,w],dtype='uint8')
arr3=np.zeros([h,w],dtype='uint8')
arr4=np.zeros([h,w],dtype='uint8')
arr5=np.zeros([h,w],dtype='uint8')
arr6=np.zeros([h,w],dtype='uint8')
arr7=np.zeros([h,w],dtype='uint8')
arr8=np.zeros([h,w],dtype='uint8')
binarr=np.zeros([h*w])


for i in range(0,h):
    for j in range(0,w):
        arr8[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2

for i in range(0,h):
    for j in range(0,w):
        arr7[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2


for i in range(0,h):
    for j in range(0,w):
        arr6[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2

for i in range(0,h):
    for j in range(0,w):
        arr5[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2


for i in range(0,h):
    for j in range(0,w):
        arr4[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2


for i in range(0,h):
    for j in range(0,w):
        arr3[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2

for i in range(0,h):
    for j in range(0,w):
        arr2[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2


for i in range(0,h):
    for j in range(0,w):
        arr1[i][j]=(img[i][j]%2)*255
        img[i][j]=img[i][j]/2

cv2.imshow('img1',arr1)
cv2.waitKey(5000)
cv2.imshow('img2',arr2)
cv2.waitKey(5000)
cv2.imshow('img3',arr3)
cv2.waitKey(5000)
cv2.imshow('img4',arr4)
cv2.waitKey(5000)
cv2.imshow('img5',arr5)
cv2.waitKey(5000)
cv2.imshow('img6',arr6)
cv2.waitKey(5000)
cv2.imshow('img7',arr7)
cv2.waitKey(5000)
cv2.imshow('img8',arr8)
cv2.waitKey(5000)
