import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def selfGrayConversion(img):
    h, w, c=img.shape
    grayImage=np.array([[0]*w]*h, 'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage

def selfAverageFilter (img, mask, sr, sc):   # (sr, sc): co-ordinate of reference point
    mh, mw=mask.shape
    ih, iw=img.shape
    newImage=img
    #Finding mask weight sum
    maskWt=0.0
    for i in range(0, mh):
        for j in range(0, mw):
            maskWt+=mask[i][j]
            
    for i in range(sr, ih+sr-(mh-1)):
        for j in range (sc, iw+sc-(mw-1)):
            sumVal=0.0
            for k in range (0, mh):
                for l in range (0, mw):
                    sumVal+=img[i-sr+k][j-sc+l]*mask[k][l]
            newImage[i][j]=sumVal/maskWt
    return newImage        

def selfimagerotate(img,h,w,deg):
    newH=math.ceil(abs(h*math.cos(deg))+abs(w*math.sin(deg)))+1
    newW=math.ceil(abs(h*math.sin(deg))+abs(w*math.cos(deg)))+1

    print("new height is= ",newH)
    print("new weight is= ",newW)

    output=np.zeros([newH,newW],'uint8')
    for i in range(newH):
        for j in range(newW):
            output[i][j]=255

    originalcentreh=round(math.ceil((h+1)/2)-1)
    originalcentrew=round(math.ceil((w+1)/2)-1)

    newcentreh=round(math.ceil((newH+1)/2)-1)
    newcentrew=round(math.ceil((newW+1)/2)-1)

    for i in range(h):
        for j in range(w):
            x=h-i-originalcentreh
            y=w-j-originalcentrew
            
            newx=round(x*math.cos(deg)-y*math.sin(deg))
            newy=round(x*math.sin(deg)+y*math.cos(deg))
            
            newx=newcentreh-newx
            newy=newcentrew-newy
            
            if 0 <= newx < newH and 0 <= newy < newW:
                output[newx][newy]=img[i][j]
    
    return output

def calcmedian(array,mh,mw):
    n=mh*mw
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    if(n%2==1):
        pos=(int)((n+1)/2)
        return array[pos-1]
    else:
        pos=(int)(n/2)
        avg=(int)((array[pos-1]+array[pos])/2)
        return avg

#Weighted average filter function... To get other mask based operation just change in this function
def selfmedianFilter (img, mask,sr,sc):   # (sr, sc): co-ordinate of reference point
    mh, mw=mask.shape
    ih, iw=img.shape
    newImage=img

    array=np.zeros(mh*mw)        
    for i in range(sr, ih+sr-(mh-1)):
        for j in range (sc, iw+sc-(mw-1)):
            t=0
            for k in range (0, mh):
                for l in range (0, mw):
                    array[t]=img[i-sr+k][j-sc+k]*mask[k][l]
                    t=t+1
            newImage[i][j]=calcmedian(array,mh,mw)
    return newImage                   
    
img =cv2.imread("einstein.jpg")
img=np.array(img)

img=selfGrayConversion(img)
cv2.imshow('grayscaleimage', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

deg=int(input("Enter the degrees by which you want to rotate: "))
deg=math.radians(deg)

h=len(img)
w=len(img[0])
print('Original Input Image Dimension: '+'height: ', h, 'width: ', w)

mask=np.zeros((3,3),'uint8')
mask[0][0]=1
mask[0][1]=1
mask[0][2]=1
mask[1][0]=1
mask[1][1]=1
mask[1][2]=1
mask[2][0]=1
mask[2][1]=1
mask[2][2]=1

'''mask=np.zeros((5,5),'uint8')
mh=5
mw=5
for i in range(mh):
    for j in range(mw):
        mask[i][j]=1'''


newH=math.ceil(abs(h*math.cos(deg))+abs(w*math.sin(deg)))+1
newW=math.ceil(abs(h*math.sin(deg))+abs(w*math.cos(deg)))+1
result=np.zeros([newH,newW],'uint8')
result=selfimagerotate(img,h,w,deg)
result=selfmedianFilter(result,mask,1,1)
#result=selfAverageFilter(result,mask,1,1)
cv2.imshow('Rotated image',result)
cv2.waitKey(5000)
cv2.destroyAllWindows()