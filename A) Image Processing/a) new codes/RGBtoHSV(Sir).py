import cv2
import numpy as np


def selfMax(a, b):
    if(a>b):
        return a
    else:
        return b
def selfMin(a, b):
    if(a>b):
        return b
    else:
        return a
    
def selfRGB2HSV(b, g, r):
    b1=b/255.0
    g1=g/255.0
    r1=r/255.0

    maxx=selfMax(selfMax(b1, g1), r1)
    minn=selfMin(selfMin(b1, g1), r1)
    diff=maxx-minn
    
    if diff == 0:  
        h = 0      
    # if maxx equal r1 then compute h 
    elif maxx == r1:  
        h = 60 * ((g1 - b1) / diff) 
  
    # if maxx equal g1 then compute h 
    elif maxx == g1: 
        h = 60 * ((b1 - r1) / diff + 2)
  
    # if maxx equal b1 then compute h 
    elif maxx == b1: 
        h = 60 * ((r1- g1) / diff+ 4)

    # if cmax equal zero 
    if maxx == 0: 
        s = 0
    else: 
        s = (diff / maxx)

    v=maxx
    if(h<0):
        h=h+360.0
    return h,s,v    



img =cv2.imread("1.jpg")
img=np.array(img)
ht, wd, c = img.shape
print('Height:  ', ht, 'Width', wd, 'Channel', c)
cv2.imshow('origImage', img)

hsvImage=np.zeros((ht, wd, 3), 'uint8')

h, s, v=selfRGB2HSV(img[0][0][0], img[0][0][1], img[0][0][2])
print('h:  ', round(h*255), 's:', round(s*255), 'v:', round(v*255))

for i in range(ht):
    for j in range (wd):
        h, s, v=selfRGB2HSV(img[i][j][0], img[i][j][1], img[i][j][2])
        hsvImage[i][j][0]=round((h/2))
        hsvImage[i][j][1]=round(s*255)
        hsvImage[i][j][2]=round(v*255)
        
hsvImage1=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('selfHSVImage',  hsvImage)
cv2.imshow('libraryHSVImage',  hsvImage1)
cv2.waitKey(0)   
cv2.destroyAllWindows()

