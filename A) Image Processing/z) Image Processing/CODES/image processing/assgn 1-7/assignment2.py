import cv2
import numpy as np
img = cv2.imread('weighted_grayscale.jpeg')
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth=img.dtype
if bit_depth=='uint8':
	bit_depth = 8
L = 2**bit_depth - 1
for i in range(0,channels):
	for j in range(0,height):
		for k in range(0,width):
			img[j][k][i] = L - img[j][k][i]
cv2.imwrite('negative_greyscale.jpeg',img)


#	     height  width  channels
#			[913][1300][3]
# image[2] as [blue][green][red]
#		
# print(len(img[0][0]))
# print((img[0][0][]))
# for row in img:
# 	for col in row:
# 		print(size(col)

