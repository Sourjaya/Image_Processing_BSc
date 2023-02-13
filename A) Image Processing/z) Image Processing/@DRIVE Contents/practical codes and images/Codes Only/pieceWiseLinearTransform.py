import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to map each intensity level to output intensity level. 
def transformedIntensity(intensity, r1, s1, r2, s2):
#intensity ---> pixel intensity ; 
    if (0 <= intensity and intensity <= r1): 
        return (s1 / r1)*intensity 
    elif (r1 < intensity and intensity <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (intensity - r1) + s1 
    else: 
        return ((255 - s2)/(255 - r2)) * (intensity  - r2) + s2 

img =cv2.imread("1.png", 0)
h, w = img.shape
print ('height= ', h)
print ('width= ', w)
print('shape', img.shape)
newImage=np.zeros((h, w), dtype = 'uint8')

for i in range(h):
    for j in range (w):
        newImage[i, j]=transformedIntensity(img[i, j], 100, 50, 200, 50)

cv2.imshow('transformed Image', newImage)   
cv2.imwrite('tImage.png', newImage);   #Specify entire pathName to write in specific directory
cv2.waitKey(0)   
cv2.destroyAllWindows()

#plt.show()
