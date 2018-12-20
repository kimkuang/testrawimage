# ===================================
# Import the libraries
# ===================================
import numpy as np
from matplotlib import pylab as plt
import cv2
#import imaging
import utility
import os,sys


# ===================================
# raw image and set up the metadata
# ===================================
image_name = "F:/git/ISP/image_process_v0.0/images/8034.raw"
input_bits = 10
input_format = "rggb"
input_width = 3264
input_height = 2448
output_bits = 8
# 利用numpydefromfile函数读取raw文件，并指定数据格式
# imgData = np.fromfile("F:/git/ISP/image_process_v0.0/images/" + image_name + ".raw", dtype=type)
imageData_0, data_4chennels = utility.readRawData(image_name, input_bits, input_format, input_width, input_height, output_bits)

ratio = 2**(input_bits - 8)

'''
#imgData = imgData.reshape(height, width, channels)
imgData = imgData / 4

imageData_0 = np.zeros((height*width*3),dtype="uint8")

i, j, k = 0, 0, 0
while k < (height-1):
    n = k*width*3+width*3
    while i < n:
        imageData_0[i+2] = imgData[j]
        imageData_0[i+4] = imgData[j+1]
        imageData_0[i+width*3+1] = imgData[j+width]
        imageData_0[i+width*3+3] = imgData[j+1+width]
        i = i + 6
        j = j + 2
    j = j + width
    k = k + 2
    i = i + width*3
'''
#imageData_0 = imageData_0.reshape(input_height, input_width, 3)
'''
imageData_0 = np.zeros((height, width, 3),dtype="uint8")


i = 0
while i < height :
    j = 0
    while j < width :
        imageData_0[i][j][2] = imgData[i][j][0]
        j = j + 2
    i = i + 2

i = 1
while i < height :
    j = 0
    while j < width :
        imageData_0[i][j][1] = imgData[i][j][0]
        j = j + 2
    i = i + 2

i = 0
while i < height :
    j = 1
    while j < width :
        imageData_0[i][j][1] = imgData[i][j][0]
        j = j + 2
    i = i + 2

i = 1
while i < height :
    j = 1
    while j < width :
        imageData_0[i][j][0] = imgData[i][j][0]
        j = j + 2
    i = i + 2
'''

cv2.imwrite('F:/git/ISP/image_process_v0.0/images/8034_test_color.bmp', (imageData_0 / ratio))


# 展示图像
#cv2.imshow('img',imageData_0)
# 注意到这个函数只能显示uint8类型的数据，如果是uint16的数据请先转成uint8。否则图片显示会出现问题。**
#cv2.waitKey()
#cv2.destroyAllWindows()

