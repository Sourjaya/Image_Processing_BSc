import cv2
import numpy as np
import matplotlib.pyplot as plt

t= np.arange(0, 10, 0.1)
y= np.sin(t)

#plt.subplot(3,1, 1)
plt.plot(t, y)
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude = sin(time)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
#plt.show()

y1=y
for i in range (1, len(t)):
    y1[i]=y[i]-y[i-1]

#plt.subplot(3, 1, 2)
plt.plot(t, y1)
#plt.title('Sine wave')
#plt.xlabel('Time')
#plt.ylabel('Amplitude = sin(time)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
#plt.show()

y2=y1
for i in range (1, len(t)):
    y2[i]=y1[i]-y1[i-1]

#plt.subplot(3, 1, 2)
plt.plot(t, y1)
#plt.title('Sine wave')
#plt.xlabel('Time')
#plt.ylabel('Amplitude = sin(time)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()  
