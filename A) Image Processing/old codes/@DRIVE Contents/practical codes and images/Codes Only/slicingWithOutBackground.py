import cv2
import numpy as np


def selfGrayConversion(img):
    h, w, c=img.shape
    grayImage=np.array([[0]*w]*h, 'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage



img1 =cv2.imread("3.jpg")
img1=np.array(img1)

h1, w1, c1 = img1.shape
print('width:  ', w1)
print('height: ', h1)
print('channel:', c1)

grayImage1=selfGrayConversion(img1)

resImg=np.zeros((h1, w1), 'uint8')

for i in range(h1):
    for j in range (w1):
        if (grayImage1[i][j]<50):         #i<newH/2 and j<newW/2  
            resImg[i][j]=0
        else:
            resImg[i][j]=grayImage1[i][j]
      

#print(rImage)
cv2.imshow('NewImage', resImg)

cv2.waitKey(0)   
cv2.destroyAllWindows()

