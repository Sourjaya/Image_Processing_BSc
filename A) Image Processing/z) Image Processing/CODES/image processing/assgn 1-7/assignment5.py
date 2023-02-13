import cv2
import numpy as np
img = cv2.imread('coc.jpeg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth=img.dtype
if bit_depth=='uint8':
	bit_depth = 8
L = 2**bit_depth - 1
redImage = np.zeros([height, width,channels],dtype='uint8')
blueImage = np.zeros([height, width,channels],dtype='uint8')
greenImage = np.zeros([height, width,channels],dtype='uint8')

gray_redImage = np.empty([height, width],dtype='uint8')
gray_blueImage = np.empty([height, width],dtype='uint8')
gray_greenImage = np.empty([height, width],dtype='uint8')


for j in range(0,height):
	for k in range(0,width):
		blueImage[j][k][0] = img[j][k][0]
		greenImage[j][k][1] = img[j][k][1]
		redImage[j][k][2] = img[j][k][2]

for j in range(0,height):
	for k in range(0,width):
		gray_blueImage[j][k] = img[j][k][0]
		gray_greenImage[j][k] = img[j][k][1]
		gray_redImage[j][k] = img[j][k][2]


# cv2.imshow('blue_channel_coc.jpeg',blueImage)
# cv2.imshow('green_channel_coc.jpeg',greenImage)
# cv2.imshow('red_channel_coc.jpeg',redImage)

# cv2.imshow('gray_blue_channel_coc.jpeg',gray_blueImage)
# cv2.imshow('gray_green_channel_coc.jpeg',gray_greenImage)
# cv2.imshow('gray_red_channel_coc.jpeg',gray_redImage)

cv2.imshow('blue_channel_coc.jpeg',blueImage)
cv2.imshow('green_channel_coc.jpeg',greenImage)
cv2.imshow('red_channel_coc.jpeg',redImage)

cv2.imshow('gray_blue_channel_coc.jpeg',gray_blueImage)
cv2.imshow('gray_green_channel_coc.jpeg',gray_greenImage)
cv2.imshow('gray_red_channel_coc.jpeg',gray_redImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
