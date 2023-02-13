import numpy as np
import cv2
import random
import math
#mean=128
#stddeviation=20
def selfIntensityNormalize(img):
    h, w=img.shape
    newImage=np.zeros([h,w],'uint8')
    maxx=np.max(img)
    minn=np.min(img)
    print("max is= ",maxx)
    print("min is= ",minn)
    diff=maxx-minn
    if(maxx==0 and minn==0):
        diff=1
    for i in range (h):
        for j in range (w):
            newImage[i][j]=int(round(255*(img[i][j]-minn)/(diff)))

    return newImage

def selfColorToGray(img):
    h, w, c = img.shape
    grayImage=np.zeros((h, w),  'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage

def selfgaussiannoise(img,mean,stddeviation):
    #pdfval=(1/((math.sqrt(2*3.14)*stddeviation)))*(math.exp((-1*(img-mean)*(img-mean))/(2*stddeviation*stddeviation)))
    x = (float(img - mean) / stddeviation)
    pdfval=(math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi)) / stddeviation
    return pdfval
    
    
img=cv2.imread('24bitexplosion.jpg')
grayImage=selfColorToGray(img)
cv2.imshow('Grayscale Image',grayImage)
cv2.waitKey(5000)
cv2.destroyAllWindows()
h=len(img)
w=len(img[0])
mean=128    
stddeviation=20
'''gaussiannoise=np.zeros((h,w),'uint8')
for i in range(h):
    for j in range(w):
        gaussiannoise[i][j]=selfgaussiannoise(grayImage[i][j],mean,stddeviation)

gaussiannoise=selfIntensityNormalize(gaussiannoise)
cv2.imshow('Gaussian noise',gaussiannoise)
print("Max noise is=",np.max(gaussiannoise))
cv2.waitKey(5000)
cv2.destroyAllWindows()

for i in range(h):
    for j in range(w):
        gaussiannoise[i][j]=gaussiannoise[i][j]+grayImage[i][j]
        
cv2.imshow('Gaussian noise',gaussiannoise)
print("Max noise is=",np.max(gaussiannoise))
cv2.waitKey(5000)
cv2.destroyAllWindows()'''

gaussian_noise=np.zeros((h,w),'uint8')
cv2.randn(gaussian_noise,mean,stddeviation)
gaussian_noise=selfIntensityNormalize(gaussian_noise)  #very important
#gaussian_noise=gaussian_noise.astype('uint8')
cv2.imshow('Gaussian noise',gaussian_noise)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()
for i in range(h):
    for j in range(w):
        gaussian_noise[i][j]=gaussian_noise[i][j]+grayImage[i][j]
   
cv2.imshow('Gaussian_noise',gaussian_noise)
print("Max noise is=",np.max(gaussian_noise))
cv2.waitKey(5000)
cv2.destroyAllWindows()
