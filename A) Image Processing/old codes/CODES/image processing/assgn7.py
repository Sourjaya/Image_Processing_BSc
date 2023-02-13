# brightness contrast
from matplotlib import pyplot as plt
import cv2
import numpy as np
import math

img = cv2.imread('coc.jpg',0)
height = len(img)
width = len(img[0])
# channels = len(img[0][0])
bit_depth=img.dtype
if bit_depth=='uint8':
    bit_depth = 8
L = 2**bit_depth - 1
histogram = np.zeros([256],dtype='long')
for j in range(0,height):
    for k in range(0,width):
        intensity = img[j][k]
        histogram[intensity] += 1

print(histogram)
plt.plot(histogram)
print("Max of histogram = " + str(np.max(histogram)))
plt.ylabel('count of pixels')
plt.xlabel('intensity values')
plt.show()

#cv2.imwrite('weighted_greyscale.jpeg',greyImage)
