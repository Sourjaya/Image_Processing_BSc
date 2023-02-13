import cv2
import  numpy as np

img=cv2.imread('1.tif')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h,w,c=img.shape
print("Height : ",h)
print("Width : ",w)
print("Channel : ",c)

img_hsv1 = np.zeros([h,w,c],dtype='uint8')

for i in range(h):
    for j in range(w):
        b=img[i][j][0]/255.0
        g=img[i][j][1]/255.0
        r=img[i][j][2]/255.0
        v=max(r,g,b)
        if(v==0):
            s=0.0
        else:
            s=(v-min(r,g,b))/(1.0*v)
        if(v==r):
            if(v-min(r,g,b)!=0):
                h= 60* (g-b)/(1.0*(v-min(r,g,b)))
            else:
                h= 60* (g-b)
        elif (v==g):
            if(v-min(r,g,b)!=0):
                h=120 + 60 * (b-r)/(1.0*(v-min(r,g,b)))
            else:
                h=120 + 60 * (b-r)
        else:
            if(v-min(r,g,b)!=0):
                h=240 + 60 * (r-g)/(1.0*(v-min(r,g,b)))
            else:
                h=240 + 60 * (r-g)
        if(h<0):
            h=h+360.0
        img_hsv1[i][j][2]=int(v*255.0)
        img_hsv1[i][j][1]=int(s*255.0)
        img_hsv1[i][j][0]=int(h/2.0)

cv2.imshow('image1',img_hsv)
cv2.imshow('image2',img_hsv1)
