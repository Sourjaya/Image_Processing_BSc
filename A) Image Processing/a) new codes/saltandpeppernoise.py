import numpy as np
import cv2
import random

def selfColorToGray(img):
    h, w, c = img.shape
    grayImage=np.zeros((h, w),  'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage

def selfsaltpeppernoise(img,prob):
    h=len(img)
    w=len(img[0])
    output=np.zeros((h,w),'uint8')
    thres=1-prob
    for i in range(h):
        for j in range(w):
            rdn=random.random()
            if rdn<prob:
                output[i][j]=0
            elif rdn>thres:
                output[i][j]=255
            else:
                output[i][j]=img[i][j]

    return output

img=cv2.imread('24bitexplosion.jpg')
grayImage=selfColorToGray(img)
cv2.imshow('Grayscale Image',grayImage)
cv2.waitKey(5000)
cv2.destroyAllWindows()
h=len(grayImage)
w=len(grayImage[0])
noise_img=np.zeros((h,w),'uint8')
noise_img=selfsaltpeppernoise(grayImage,0.05)
cv2.imshow('Salt Pepper Noisy Image',noise_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()