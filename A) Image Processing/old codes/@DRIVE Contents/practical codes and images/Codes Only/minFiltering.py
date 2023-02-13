import cv2
import numpy as np

def calculateMin(array):
    minimum=256
    for i in range(9):
        if(array[i]<minimum):
            minimum=array[i]
    return minimum

img =cv2.imread("1.jpg")
img=np.array(img)

h, w, c = img.shape

grayImage=np.array([[0]*w]*h, 'uint8')
minFilteredImage=np.array([[0]*w]*h, 'uint8') 


for i in range(h):
    for j in range (w):
        grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
        minFilteredImage[i][j]=grayImage[i][j]

#grayImage=grayImage/255
array=np.zeros(9)

for i in range(1, h-1):
    for j in range (1, w-1):
        t=0
        for l in range(i-1, i+2):
            for m in range(j-1, j+2):
                array[t]=grayImage[l][m]
                t=t+1
        minFilteredImage[i][j]=calculateMin(array)
        
cv2.imshow('grayComImage', grayImage)
cv2.imwrite('grayImage.tiff', grayImagegrayImage)
#cv2.waitKey(0)
cv2.imshow('Min Filtered Image', minFilteredImage)
cv2.imwrite('minFilteredImage.tiff', minFilteredImage)
cv2.waitKey(0) 
cv2.destroyAllWindows()

