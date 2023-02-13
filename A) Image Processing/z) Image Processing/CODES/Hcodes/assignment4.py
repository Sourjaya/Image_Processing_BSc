import cv2
import numpy as np
import math
img = cv2.imread('colourful.jpeg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth = 8
L = 2**bit_depth - 1
c = 2
gamma = 2
maxIntensity = 0
for i in range(0,channels):
	for j in range(0,height):
		for k in range(0,width):
			intensity = img[j][k][i]
			intensity = (c)*(intensity**gamma)
			if intensity>maxIntensity:
				maxIntensity = intensity
			intensity = intensity*255/maxIntensity
			img[j][k][i] = intensity
cv2.imwrite('gamma.jpeg',img)