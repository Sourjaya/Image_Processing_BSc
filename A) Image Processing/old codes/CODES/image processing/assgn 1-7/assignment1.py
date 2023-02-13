import cv2
import numpy as np
img = cv2.imread('colourful.jpeg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth=img.dtype
if bit_depth=='uint8':
	bit_depth = 8
L = 2**bit_depth - 1
greyImage = np.empty([height, width],dtype='uint8')

# individual colour channels as coloured plates

for j in range(0,height):
	for k in range(0,width):
		greyImage[j][k] =  0.11*img[j][k][0] + 0.59*img[j][k][1] + 0.3*img[j][k][2]

cv2.imwrite('weighted_greyscale.jpeg',greyImage)


#	     height  width  channels
#			[913][1300][3]
# image[2] as [blue][green][red]
#		