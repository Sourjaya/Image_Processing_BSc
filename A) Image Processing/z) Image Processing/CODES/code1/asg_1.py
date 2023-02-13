import cv2
import numpy as np
img = cv2.imread('abc.jpg',1)
h = len(img)
w = len(img[0])
channels = len(img[0][0])
bit_depth = 8
L = 2*bit_depth - 1
greyImage = np.empty([height, width])

for j in range(0,h):
    for k in range(0,w):
        greyImage[j][k] =  0.11*img[j][k][0] + 0.59*img[j][k][1] + 0.3*img[j][k][2]

cv2.imwrite('grey.jpg',greyImage)


#         height  width  channels
#            [913][1300][3]
# image[2] as [blue][green][red]
#
