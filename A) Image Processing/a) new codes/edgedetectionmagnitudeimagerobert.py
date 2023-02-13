import cv2
import numpy as np
import math

def selfIntensityNormalize(img):
    h, w=img.shape
    newImage=np.zeros([h,w],'uint8')
    maxx=np.max(img)
    minn=np.min(img)
    print("max is= ",maxx)
    print("min is= ",minn)
    for i in range (h):
        for j in range (w):
            newImage[i][j]=round(255*(img[i][j]-minn)/(maxx-minn))

    return newImage

#Function for pad remove
def selfPadRemoval(img, rt, rb, cl, cr):  #rt: rows top, rb=rows bottom, cl: columns left, cr: columns right
    ht, wd=img.shape
    
    newHt=img.shape[0]-rt- rb
    newWd=img.shape[1]-cl-cr
    padLessImage=np.zeros((newHt, newWd),  dtype='uint8')

    for i in range(0, newHt):
        for j in range(0, newWd):
            padLessImage[i][j]=img[i+rt][j+cl]

    return padLessImage

#selfPadRemoval ends

def selfColorToGray(img):
    h, w, c = img.shape
    grayImage=np.zeros((h, w),  'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage
    
def selfPadding(img, rt, rb, cl, cr):  #rt: rows in top, rb=rows in bottom, cl: columns in left, cr: columns in right
    ht, wd=img.shape
    
    newHt=img.shape[0]+rt+ rb   #img.shape[0]=ht
    newWd=img.shape[1]+cl+ cr   #img.shape[1]=wd
    padImage=np.zeros((newHt, newWd),  dtype='uint8')

    #Copying actual image intensities
    
    for i in range(0, ht):
        for j in range(0, wd):
            padImage[i+rt][j+cl]=img[i][j]

    #Filling top rows
    for j in range (0, newWd):
        for i in range(0, rt):
            if(j<cl): 
                padImage[i][j]=img[0][0]
            elif(j>=cl+wd):
                 padImage[i][j]=img[0][wd-1]
            else:
                padImage[i][j]=img[0][j-cl]

     #Filling bottom rows
    for j in range (0, newWd):
        for i in range(ht+rt-1, ht+rt+rb):
            if(j<cl): 
                padImage[i][j]=img[ht-1][0]
            elif(j>=cl+wd):
                 padImage[i][j]=img[ht-1][wd-1]
            else:
                padImage[i][j]=img[ht-1][j-cl]

     #Filling left columns
    for i in range (0, newHt):
        for j in range(0, cl):
            if(i<rt): 
                padImage[i][j]=img[0][0]
            elif(i>=rt+ht):
                 padImage[i][j]=img[ht-1][0]
            else:
                padImage[i][j]=img[i-rt][0]

     #Filling right columns
    for i in range (0, newHt):
        for j in range(wd+cl-1, wd+cl+cr):
            if(i<rt): 
                padImage[i][j]=img[0][wd-1]
            elif(i>=rt+ht):
                 padImage[i][j]=img[ht-1][wd-1]
            else:
                padImage[i][j]=img[i-rt][wd-1]

    return padImage

#Weighted average filter function... To get other mask based operation just change in this function
def selfFilter (img, mask, sr, sc):   # (sr, sc): co-ordinate of reference point
    mh, mw=mask.shape
    ih, iw=img.shape
    newImage=img
    #Finding mask weight sum
    #maskWt=0.0
            
    for i in range(sr, ih+sr-(mh-1)):
        for j in range (sc, iw+sc-(mw-1)):
            sumVal=0.0
            for k in range (0, mh):
                for l in range (0, mw):
                    sumVal+=img[i-sr+k][j-sc+l]*mask[k][l];
            newImage[i][j]=sumVal;
    return newImage               

img=cv2.imread('shapes.jpg')
grayImage=selfColorToGray(img)
cv2.imshow('Grayscale Image',grayImage)
cv2.waitKey(5000)
cv2.destroyAllWindows()
h=len(img)
w=len(img[0])
print('Original Input Image Dimension: '+'height: ', h, 'width: ', w)

#Reading mask height and width
mh=2
mw=2
print(mh,mw)
xmask=np.zeros((mh, mw))
ymask=np.zeros((mh, mw))
#Reading mask weights
xmask[0][0]=-1
xmask[0][1]=0
xmask[1][0]=0
xmask[1][1]=1

ymask[0][0]=0
ymask[0][1]=-1
ymask[1][0]=1
ymask[1][1]=0

        
#Reading co-ordinate of reference point
r=0
c=0
#Calculating pad amounts
rt=r   #Number of pad rows in top
cl=c   #Number of pad columns in left
rb=mh-r-1   #Number of pad rows in bottom
cr=mw-c-1   #Number of pad columns in right
grayImage=selfPadding(grayImage, rt, rb, cl, cr)  # put pad amount values as rows top, rows bottom, columns left, columns right

h, w = grayImage.shape
grayImagex=np.zeros((h,w),'uint8')
grayImagey=np.zeros((h,w),'uint8')
print('Original Pad Image Dimension: '+'height: ', h, 'width: ', w)
#Call functions for different neighborhood based filtering
grayImagex=selfFilter (grayImage, xmask, r, c)
grayImagey=selfFilter (grayImage, ymask, r, c)

grayImagex=selfPadRemoval(grayImagex, rt, rb, cl, cr)  # put pad amount values as per requirement rows in top, rows in bottom, columns in left, columns in right
grayImagey=selfPadRemoval(grayImagey, rt, rb, cl, cr)
cv2.imshow('Filtered Imagex', grayImagex)
cv2.imshow('Filtered Imagey', grayImagey)
cv2.waitKey(5000)
cv2.destroyAllWindows()

h,w=grayImagex.shape
magImage=np.zeros((h,w),'uint8')
        
for i in range(h):
    for j in range(w):
        magImage[i][j]=np.sqrt(np.power(grayImagex[i][j],2)+np.power(grayImagey[i][j],2))

'''maxx=np.max(magImage)
for i in range(h):
    for j in range(w):
        magImage[i][j]=(magImage[i][j]/maxx)'''

cv2.imshow('Magnitude Image',magImage)
sumweight=0
for i in range(h):
    for j in range(w):
        sumweight+=magImage[i][j]

avgweight=sumweight/(h*w)

edgeImage=np.zeros((h,w),'uint8')

for i in range(h):
    for j in range(w):
        if(magImage[i][j]>avgweight):
            edgeImage[i][j]=255

edgeImage=selfIntensityNormalize(edgeImage)            
cv2.imshow('Edge Image', edgeImage)
cv2.waitKey(5000)
cv2.destroyAllWindows()



