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

#rImage=np.array([[0]*w]*h, 'uint8')
#gImage=np.array([[0]*w]*h, 'uint8')
#bImage=np.array([[0]*w]*h, 'uint8')
grayImage=np.array([[0]*w]*h, 'uint8')
negImage=np.array([[0]*w]*h, 'uint8')
logImage20=np.array([[0]*w]*h, 'uint8')
logImage10=np.array([[0]*w]*h, 'uint8')

c=20

for i in range(h):
    for j in range (w):
#        rImage[i][j]=img[i][j][0]
#        gImage[i][j]=img[i][j][1]
#       bImage[i][j]=img[i][j][2]
        grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
#        negImage[i][j]=255-grayImage[i][j]
        logImage20[i][j]=50*np.log(grayImage[i][j]+1)
        logImage10[i][j]=10*np.log(grayImage[i][j]+1)
    print(logImage20[i])

        
#print(rImage)
#cv2.imshow('redComImage', rImage)
#cv2.imshow('greenComImage', gImage)
#cv2.imshow('blueComImage', bImage)
cv2.imshow('grayComImage', grayImage)
#cv2.imshow('negetiveImage', negImage)
cv2.imshow('10logImage', logImage10)
cv2.imshow('20logImage', logImage20)

cv2.waitKey(0)   
cv2.destroyAllWindows()

