import cv2
import numpy as np


def selfGrayConversion(img):
    h, w, c=img.shape
    grayImage=np.array([[0]*w]*h, 'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage



img1 =cv2.imread("1.jpg")
img1=np.array(img1)

img2=cv2.imread("24bitexplosion.jpg")
img2=np.array(img2)

h1, w1, c1 = img1.shape
print('width:  ', w1)
print('height: ', h1)
print('channel:', c1)

h2, w2, c2 = img2.shape
print('width:  ', w2)
print('height: ', h2)
print('channel:', c2)

#grayImage1=np.array([[0]*w1]*h1, 'uint8')
#grayImage2=np.array([[0]*w2]*h2, 'uint8')  


#grayImage1=selfGrayConversion(img1)
#grayImage2=selfGrayConversion(img2)

newH=256
newW=256 

# resize images
dsize = (newH, newW)
#reImg1= cv2.resize(grayImage1, dsize, interpolation = cv2.INTER_AREA)
#reImg2= cv2.resize(grayImage2, dsize, interpolation = cv2.INTER_AREA)

reImg1= cv2.resize(img1, dsize, interpolation = cv2.INTER_AREA)
reImg2= cv2.resize(img2, dsize, interpolation = cv2.INTER_AREA)

resImg=np.zeros((newH, newW, 3), 'uint8')

for i in range(newH):
    for j in range (newW):
        if (i<2*(newH/3)):         #i<newH/2 and j<newW/2  
            resImg[i][j][0]=reImg1[i][j][0]
            resImg[i][j][1]=reImg1[i][j][1]
            resImg[i][j][2]=reImg1[i][j][2]
        else:
            resImg[i][j][0]=reImg2[i][j][0]
            resImg[i][j][1]=reImg2[i][j][1]
            resImg[i][j][2]=reImg2[i][j][2]
      

#print(rImage)
cv2.imshow('NewImage', resImg)

cv2.waitKey(0)   
cv2.destroyAllWindows()

