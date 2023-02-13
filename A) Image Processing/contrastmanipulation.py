import cv2
import numpy as np

def selfColorToGray(img):
    h, w, c = img.shape
    grayImage=np.zeros((h, w),  'uint8')
    for i in range(h):
        for j in range (w):
            grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
    return grayImage

def cmanipulate(img,a,b,m,n):
    h,w,c=img.shape
    manImage=np.zeros([h,w,c],'uint8')
    factor=(n-m)/(b-a)
    if(factor>1):
        print("Contrast stretching")
    else:
        print("Contrast squeezing")
    for k in range(c):
        for i in range(h):
            for j in range(w):
                manImage[i][j][k]=m+factor*(img[i][j][k]-a)
    return manImage

img=cv2.imread("birthdayp1.jpg")
h,w,c=img.shape
newImage=np.zeros([h,w,c],'uint8')
b=np.max(img)
a=np.min(img)
print("max is= ",b)
print("min is= ",a)

print("Enter the range to contrast enhance or squeeze")
m=int(input("Minimum intensity of new Image "))
n=int(input("Maximum intensity of new Image "))
newImage=cmanipulate(img,a,b,m,n)
maxx=np.max(newImage)
minn=np.min(newImage)
print("max is= ",maxx)
print("min is= ",minn)
cv2.imwrite('original_Image.jpg',img)
cv2.imwrite('Manipulated_Image.jpg',newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
