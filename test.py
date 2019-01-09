# ===================================
# Import the libraries
# ===================================
import numpy as np
from matplotlib import pylab as plt
import cv2
#import imaging
import utility
import os,sys
from scipy import signal


image_name = '2375'

data = [[1,2,3,4,5,6,7,8],\
        [9,10,11,12,13,14,15],\
        [16,17,18,19,20,21,22,23],\
        [24,25,26,27,28,29,30,31]]

#data = np.fromfile("F:/git/ISP/image_process_v0.1/images/" + image_name + ".raw", dtype='uint16')
#data = data.reshape(1200, 1600)
data = np.asarray(data)
v = np.asarray(signal.convolve2d(data, [[1],[0],[-1]], mode="same", boundary="symm"))
h = np.asarray(signal.convolve2d(data, [[1, 0, -1]], mode="same", boundary="symm"))


print('data=',data)
print('v=',v)
#print(data)
      #,\
      #['gb','b','gb','b','gb','b','gb','b'],\
      #['r','gr','r','gr','r','gr','r','gr'],\
      #['gb','b','gb','b','gb','b','gb','b']]

#R = data[::2,::2]


#print('r=',R)