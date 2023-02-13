import cv2
import numpy as np


#Function of self padding
def selfPadding(img, rt, rb, cl, cr):  #rt: rows in top, rb=rows in bottom, cl: columns in left, cr: columns in right  img: original image
    ht, wd=img.shape
    
    newHt=img.shape[0]+rt+ rb
    newWd=img.shape[1]+cl+ cr
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

#Function of self padding ends


#Function for pad remove
def selfPadRemoval(img, rt, rb, cl, cr):  #rt: rows top, rb=rows bottom, cl: columns left, cr: columns right  img: padded Image
    ht, wd=img.shape
    
    newHt=img.shape[0]-rt- rb
    newWd=img.shape[1]-cl-cr
    padLessImage=np.zeros((newHt, newWd),  dtype='uint8')

    for i in range(0, newHt):
        for j in range(0, newWd):
            padLessImage[i][j]=img[i+rt][j+cl]

    return padLessImage

#selfPadRemoval ends

#Function for rgb to gray
def selfColorToGray(img):
    h, w, c = img.shape
    grayImage=np.zeros((h, w),  'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage

#Weighted average filter function... To get other mask based operation just change in this function
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
                    sumVal+=img[i-sr+k][j-sc+l]*mask[k][l];
            newImage[i][j]=sumVal/maskWt;
    return newImage               


#main function
img =cv2.imread("3.jpg")
img=np.array(img)

grayImage=selfColorToGray(img)

cv2.imshow('Original Image', grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

h, w = grayImage.shape
print('Original Input Image Dimension: '+'height: ', h, 'width: ', w)

#Reading mask height and width
mh, mw = map(int, input("Enter mask Height and Width separated by space: ").split())
mask=np.zeros((mh, mw))

#Reading mask weights
for i in range(0, mh):
    for j in range (0, mw):
        mask[i][j]=float(input('Enter mask weights in row major order :' ))
        
#mh, mw = map(int, input("Enter mask Height and Width: ").split())
#Reading co-ordinate of reference point
r, c= map(int, input("Enter co-ordinate of reference point: 0<=rowPos<mask Height and 0=colPos< maskWidth separated by space: ").split())

#Calculating pad amounts
rt=r   #Number of pad rows in top
cl=c   #Number of pad columns in left
rb=mh-r-1   #Number of pad rows in bottom
cr=mw-c-1   #Number of pad columns in right

grayImage=selfPadding(grayImage, rt, rb, cl, cr)  # put pad amount values as rows top, rows bottom, columns left, columns right
h, w = grayImage.shape
print('Original Pad Image Dimension: '+'height: ', h, 'width: ', w)

#Call functions for different neighborhood based filtering
grayImage=selfAverageFilter (grayImage, mask, r, c)

grayImage=selfPadRemoval(grayImage, rt, rb, cl, cr)  # put pad amount values as per requirement rows in top, rows in bottom, columns in left, columns in right
cv2.imshow('Filtered Image', grayImage)
h, w = grayImage.shape
print('Final Input Image Dimension: '+'height: ', h, 'width: ', w)
#print('height: ', h, 'width:', w)
