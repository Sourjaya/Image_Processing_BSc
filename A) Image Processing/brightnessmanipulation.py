import cv2
import numpy as np

def bmanipulate(img,ch):
    if(ch==1):
        a=int(input("Enter value of a (co-efficient of x)"))
        b=int(input("Enter value of b (constant)"))
        h,w=img.shape
        manImage=np.zeros([h,w])
        for i in range(h):
            for j in range(w):
                manImage[i][j]=a*img[i][j]+b
        return manImage
        
    elif(ch==2):
        a=a=int(input("Enter value of a (co-efficient of x^2)"))
        b=int(input("Enter value of b (co-efficient of x)"))
        c=int(input("Enter value of c (constant)"))
        h,w=img.shape
        manImage=np.zeros([h,w])
        for i in range(h):
            for j in range(w):
                manImage[i][j]=a*pow(img[i][j],2)+b*img[i][j]+c
        return manImage
        


def selfIntensityNormalize(img):
    h,w=img.shape
    newImage=np.zeros([h,w],'uint8')
    maxx=np.max(img)
    minn=np.min(img)
    print("max is= ",maxx)
    print("min is= ",minn)
    if(maxx==minn):
        return newImage
    else:
        for i in range (h):
            for j in range (w):
                newImage[i][j]=abs(round(255*(img[i][j]-minn)/(maxx-minn)))

        return newImage

img=cv2.imread("birthdayp1.jpg",0)
h,w=img.shape
newImage=np.zeros([h,w],'uint8')

ch=int(input("Enter 1 for Linear or 2 for Non-linear transformation"))
newImage=bmanipulate(img,ch)
newImage=selfIntensityNormalize(newImage)
maxx=np.max(newImage)
minn=np.min(newImage)
print("max is= ",maxx)
print("min is= ",minn)
cv2.imshow("original_Image",img)
cv2.imwrite("Manipulated_Image1.jpg", newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
