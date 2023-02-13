import cv2
import numpy as np
import matplotlib.pyplot as plt

#Function for rgb to gray
def selfColorToGray(img):
    h, w, c = img.shape
    grayImage=np.zeros((h, w),  'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage

def generateNormalizedHistogram(img):
    h, w=img.shape
    histogram=np.zeros(256, 'float')
    
    for i in range(0, h):
        for j in range(0, w):
            histogram[img[i][j]]+=1
            
    for i in range(0, 256):
        histogram[i]/=(h*w)
    return histogram


def calculateCDF(hist):
    cdfHist=hist
    for i in range(1, 256):
        cdfHist[i]+=cdfHist[i-1]
    return cdfHist

def generateEqualizedIntensities(cdf):
    equalizedIntensities=np.zeros(256, 'uint8')
    for i in range(0, 256):
        equalizedIntensities[i]=np.floor(255*(cdf[i]-cdf[0])/(cdf[255]-cdf[0])+0.5)
    return equalizedIntensities

def generateEqualizedImage(img, intensity):
    h,w=img.shape
    newImage=np.zeros((h, w), 'uint8')
    for i in range(0,h):
        for j in range (0, w):
            t=img[i][j]
            newImage[i][j]=intensity[t]
    return newImage
            
#main function
img =cv2.imread("1.jpg")
img=np.array(img)

grayImage=selfColorToGray(img)
cv2.imshow('Original Image', grayImage)

normalizedHistogram=generateNormalizedHistogram(grayImage)
#print(normalizedHistogram)

plt.subplot(1, 3,1)
plt.plot(normalizedHistogram)
plt.title('Actual Histogram (Normalized)')
plt.ylabel('frequency')
plt.xlabel('intensity')


cdfHistogram=calculateCDF(normalizedHistogram)
#print(cdfHistogram)

plt.subplot(1, 3,2)
plt.plot(cdfHistogram)
plt.title('CDF Plot')
plt.xlabel('intensity')
plt.ylabel('frequency')


transformedIntensities=generateEqualizedIntensities(cdfHistogram)
#print(transformedIntensities)
transformedImage=generateEqualizedImage(grayImage, transformedIntensities)
equalizedHistogram=generateNormalizedHistogram(transformedImage)

plt.subplot(1, 3,3)
plt.plot(equalizedHistogram)
plt.title('Histogram Equalized Histogram (Normalized )')
plt.xlabel('intensity')
plt.ylabel('frequency')

cv2.imshow('Histogram Equalized Image', transformedImage)

plt.show()

