# brightness contrast
import cv2
import numpy as np
import math

img = cv2.imread('gray_blue_channel_coc.jpeg',0)
height = len(img)
width = len(img[0])
bit_depth=img.dtype
if bit_depth=='uint8':
	bit_depth = 8
L = 2**bit_depth - 1

total_number_of_pixels = height*width
brightness = 0
for j in range(0,height):
	for k in range(0,width):
		brightness += img[j][k]

contrast = np.std(img)
brightness /= total_number_of_pixels
print("brightness = " + str(brightness))
print("contrast = " + str(contrast))
