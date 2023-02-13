import cv2
import numpy as np


def selfImageAdd (im1, im2):
    h, w=im1.shape
    newImage=np.array([[0]*w]*h)
    for i in range (h):
        for j in range (w):
            newImage[i][j]=im1[i][j]+im2[i][j]
    return newImage

def selfIntensityNormalize(img):
    h, w=img.shape
    newImage=np.array([[0]*w]*h, 'uint8')
    maxx=np.max(img)
    minn=np.min(img)
    
    for i in range (h):
        for j in range (w):
            newImage[i][j]=round(255*(img[i][j]-minn)/(maxx-minn))

    return newImage



img1 =cv2.imread("1.tif")
img2 =cv2.imread("2.tif")

#conversion to numpy array
img1=np.array(img1)
img2=np.array(img2)

h1, w1, c1 = img1.shape
print('width:  ', w1)
print('height: ', h1)
print('channel:', c1)

h2, w2, c2= img2.shape
print('width:  ', w2)
print('height: ', h2)
print('channel:', c2)

#Performing Image resize on img1: new dimension is same as img2
dim = (w2, h2)   # change here
img1= cv2.resize(img1, dim, interpolation = cv2.INTER_CUBIC)

grayImage1=np.array([[0]*w2]*h2)
grayImage2=np.array([[0]*w2]*h2)
newImage=np.array([[0]*w2]*h2)

for i in range(h2):
    for j in range (w2):
        grayImage1[i][j]=0.11*img1[i][j][0]+0.59*img1[i][j][1]+0.3*img1[i][j][2]
        grayImage2[i][j]=0.11*img2[i][j][0]+0.59*img2[i][j][1]+0.3*img2[i][j][2]

newImage=selfImageAdd (grayImage1, grayImage2)
newImage=selfIntensityNormalize(newImage)
cv2.imshow('Aditive Image', newImage)


