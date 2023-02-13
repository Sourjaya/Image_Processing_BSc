import cv2
import numpy as np

'''def maxm(a):
    max1=a[0]
    for i in range(1,9):
        if a[i]>max1:
            max1=a[i]
    return max1 '''       

img =cv2.imread("coc.jpg", 0)
h, w = img.shape
print ('height= ', h)
print ('width= ', w)
print('shape', img.shape)
newImage=np.zeros((h, w), dtype = 'uint8')
#a=np.zeros(9,dtype='uint8')
t=0
"""for i in range(h):
    for j in range (w):
        newImage[i, j]=img[i, j]"""
maxm=0       
for i in range(1,h-1):
    for j in range (1,w-1):
        #minm=img[i-1][j-1]
        for l in range(i-1,i+2):
            #print(l)
            for m in range (j-1,j+2):
                #print(m)
                #print(newImage[l][m])
                if img[l][m]>maxm:
                    maxm=img[l][m]
        newImage[i][j]=maxm
        maxm=0
cv2.imshow('transformed Image', newImage)
cv2.waitKey(0)   
cv2.destroyAllWindows()
