import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread("1.jpg")
img=np.array(img)

h, w, c = img.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)

#print (img)

#rImage=np.array([[0]*w]*h, 'uint8')
#gImage=np.array([[0]*w]*h, 'uint8')
#bImage=np.array([[0]*w]*h, 'uint8')
grayImage=np.array([[0]*w]*h, 'uint8')

hist=np.zeros(256)


for i in range(h):
    for j in range (w):
        grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]
        
#    print(logImage20[i])
#grayImage=float(grayImage)

s=0.0
ss=0.0
for i in range(h):
    for j in range (w):
        hist[grayImage[i][j]]=hist[ grayImage[i][j]]+1

maximum=max(hist)
print('Maximum=', maximum);

#Normalized histogram

#for i in range (256):
#    hist[i]=hist[i]/maximum;
    
print(hist)

plt.plot(hist);
plt.ylabel('frequency')
plt.xlabel('intensity')
plt.show()

cv2.imshow('grayComImage', grayImage)

cv2.waitKey(0)   
cv2.destroyAllWindows()

