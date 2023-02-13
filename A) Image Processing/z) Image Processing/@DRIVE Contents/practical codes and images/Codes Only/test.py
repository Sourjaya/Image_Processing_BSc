import cv2
import numpy as np

img =cv2.imread("1.tif")
img=np.array(img)

h, w, c = img.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)

#print (img)
cv2.imshow('origImage', img)
#cv2.waitKey(0)

rImage=np.array([[0]*w]*h, 'uint8')
gImage=np.array([[0]*w]*h, 'uint8')
bImage=np.array([[0]*w]*h, 'uint8')

for i in range(h):
    for j in range (w):
        rImage[i][j]=img[i][j][0]
        gImage[i][j]=img[i][j][1]
        bImage[i][j]=img[i][j][2]
#    print(rImage[i])
        
#print(rImage)
cv2.imshow('redComImage', rImage)
cv2.imshow('greenComImage', gImage)
cv2.imshow('blueComImage', bImage)
cv2.waitKey(0)   
cv2.destroyAllWindows()

