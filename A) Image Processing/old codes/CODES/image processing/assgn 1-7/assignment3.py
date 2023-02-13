import cv2
import numpy as np
import math
img = cv2.imread('colourful.jpeg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth=img.dtype
if bit_depth=='uint8':
	bit_depth = 8
L = 2**bit_depth - 1
c = 50
for i in range(0,channels):
	for j in range(0,height):
		for k in range(0,width):
			intensity = img[j][k][i]
			intensity = c*(math.log(1+intensity,10))
			img[j][k][i] = intensity
cv2.imwrite('log.jpeg',img)
