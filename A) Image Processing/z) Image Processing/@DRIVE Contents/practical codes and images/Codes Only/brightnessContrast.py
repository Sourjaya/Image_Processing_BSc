import cv2
import numpy as np

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


for i in range(h):
    for j in range (w):
        grayImage[i][j]=0.11*img[i][j][0]+0.59*img[i][j][1]+0.3*img[i][j][2]

#grayImage=grayImage/255
        
#for i in range(h):
   # for j in range (w):
    #    grayImage[i][j]=grayImage[i][j]/255

#    print(logImage20[i])
#grayImage=float(grayImage)
s=0.0
ss=0.0
for i in range(h):
    for j in range (w):
        s=s+grayImage[i][j]

brightness=s/(h*w)

for i in range (h):
    for j in range (w):        
        ss=ss+(grayImage[i][j]-brightness)*(grayImage[i][j]-brightness)

contrast=np.sqrt(ss/(h*w))

print('brightness', brightness)
print('contrast', contrast)

#print(rImage)
cv2.imshow('grayComImage', grayImage)

cv2.waitKey(0)   
cv2.destroyAllWindows()

