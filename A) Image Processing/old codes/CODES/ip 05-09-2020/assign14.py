import cv2
import numpy as np

def mean(a):
    mean1=0.0
    sum1=0.0
    for i in range(0,9):
        sum1=sum1+a[i]
    mean1=sum1/9.0
    return mean1
img =cv2.imread("coc.jpg", 0)
cv2.imshow('original',img)
h, w = img.shape
print ('height= ', h)
print ('width= ', w)
print('shape', img.shape)
newImage=np.zeros((h, w), dtype = 'uint8')
a=np.zeros(9)
#print(a)
for i in range(1,h-1):
    for j in range (1,w-1):
        #print(i,j)
        t=0
        for l in range(i-1,i+2):
            for m in range(j-1,j+2):
                a[t]=img[l][m]
                t=t+1
        newImage[i][j]=mean(a)
cv2.imshow('meanfilter',newImage)
cv2.imwrite('meanfilter.jpg',newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
