import cv2
import numpy as np
img = cv2.imread('abc.jpg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth = 8
L = 2*bit_depth - 1
redImage = np.empty([height, width,channel])

for j in range(0,height):
    for k in range(0,width):
        rimage[]

cv2.imwrite('custom_greyscale.jpg',greyImage)


#         height  width  channels
#            [913][1300][3]
# image[2] as [blue][green][red]
#
