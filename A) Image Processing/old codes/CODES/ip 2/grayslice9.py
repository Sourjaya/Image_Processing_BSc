import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to map each intensity level to output intensity level. 
def transformedIntensity(intensity):
#intensity ---> pixel intensity ; 
    if (50 <= intensity and intensity <= 95): 
        return 100 
    elif (100 <= intensity and intensity <= 170): 
        return 200
    elif (210 <= intensity and intensity <= 255): 
        return 255 
    else: 
        return intensity 

img =cv2.imread("coc.jpg", 0)
h, w = img.shape
print ('height= ', h)
print ('width= ', w)
print('shape', img.shape)
newImage=np.zeros((h, w), dtype = 'uint8')

for i in range(h):
    for j in range (w):
        newImage[i, j]=transformedIntensity(img[i, j])

cv2.imshow('transformed Image', newImage)   
#cv2.imwrite('tImage.png', newImage);   #Specify entire pathName to write in specific directory
cv2.waitKey(0)   
cv2.destroyAllWindows()

#plt.show()
