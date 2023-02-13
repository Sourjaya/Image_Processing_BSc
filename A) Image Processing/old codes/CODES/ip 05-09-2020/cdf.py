import cv2
import numpy as np
import matplotlib.pyplot as plt
def cdf(lst,n):
    a=np.zeros([n])
    a[0]=lst[0]
    for i in range(1,n):
        a[i]=a[i-1]+lst[i]
    for i in  range(0,n):
        print(a[i])
    plt.plot(a)
    plt.ylabel('output')
    plt.xlabel('input')
    plt.show()
    plt.plot(lst)
    plt.ylabel('output')
    plt.xlabel('input')
    plt.show()

n=int(input("Enter number of elements"))
lst=np.zeros([n])
print("\n Enter numbers")
for i in  range(0,n):
    lst[i]=int(input())
cdf(lst,n)