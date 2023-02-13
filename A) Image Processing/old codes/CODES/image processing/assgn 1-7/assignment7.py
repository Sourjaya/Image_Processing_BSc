# # histogram
# from matplotlib import pyplot as plt
# import cv2
# import numpy as np
# import math

# img = cv2.imread('gray_blue_channel_coc.jpeg',0)
# height = len(img)
# width = len(img[0])
# # channels = len(img[0][0])
# bit_depth=img.dtype
# if bit_depth=='uint8':
# 	bit_depth = 8
# L = 2**bit_depth - 1
# histogram = np.zeros([256],dtype='long')
# for j in range(0,height):
# 	for k in range(0,width):
# 		intensity = img[j][k]
# 		histogram[intensity] += 1

# print(histogram)
# plt.plot(histogram)
# print("Max of histogram = " + str(np.max(histogram)))
# plt.ylabel('count of pixels')
# plt.xlabel('intensity values')
# plt.show()


import cv2
import numpy as np
img = cv2.imread('coc.jpeg',1)
height = len(img)
width = len(img[0])
channels = len(img[0][0])
bit_depth = 8
L = 2**bit_depth - 1
redImage = np.zeros([height, width])
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

Message #general