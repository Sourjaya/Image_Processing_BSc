import cv2
import numpy as np
img = cv2.imread('coc.jpg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth = 8
L = 2**bit_depth - 1
redImage = np.zeros([height, width],dtype='uint8')
blueImage = np.zeros([height, width],dtype='uint8')
greenImage = np.zeros([height, width],dtype='uint8')

for j in range(0,height):
	for k in range(0,width):
		blueImage[j][k] = img[j][k][0]
		greenImage[j][k] = img[j][k][1]
		redImage[j][k] = img[j][k][2]

cv2.imshow('blue_channel_coloured',blueImage)
cv2.imshow('green_channel_coloured',greenImage)
cv2.imshow('red_channel_coloured',redImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
