import cv2
import numpy as np
import matplotlib.pyplot as plt

def cdf(lst,n):
    temp=np.zeros([n])
    temp[0]=lst[0]
    for i in range(1,n):
            temp[i]=temp[i-1]+lst[i]
    for i in range(0,n):
        print(temp[i])
    plt.plot(temp)
    plt.ylabel('output')
    plt.xlabel('input')
    plt.plot(lst)
    plt.ylabel('output')
    plt.xlabel('input')
    plt.show()
    
    
n=int(input("Enter number of elements: "))
lst=np.zeros([n])

for i in range(0,n):
    lst[i]=int(input())
cdf(lst,n)

    

