# ===================================
# Import the libraries
# ===================================
import numpy as np
from matplotlib import pylab as plt
import os,sys
import cv2

#====================================
#test list to matrix
#====================================
width, height = 6, 4
imgdata = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
imagedata_0 = np.zeros((width*height*3),'uint8')
i, j, k = 0, 0, 0
while k < (height-1):
    print('k=',k)
    print('i1=',i)
    while i < (k*width*3+width*3):
        print('j=',j)
        imagedata_0[i+2] = imgdata[j]
        imagedata_0[i+4] = imgdata[j+1]
        imagedata_0[i+width*3+1] = imgdata[j+width]
        imagedata_0[i+width*3+3] = imgdata[j+1+width]
        i = i + 6
        j = j + 2
    j = j + width
    k = k + 2
    i = i + width*3
    print('i2=',i)

print(imagedata_0)
