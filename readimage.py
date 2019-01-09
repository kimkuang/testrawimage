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
image_name = "F:/git/ISP/image_process_v0.1/images/8034.raw"
input_bits = 10
input_format = "rggb"
input_width = 3264
input_height = 2448
output_bits = 10

imageData_0, data_4chennels = utility.readRawData(image_name, input_bits, input_format, input_width, input_height)

ratio = 2**(input_bits - 8)


cv2.imwrite('F:/git/ISP/image_process_v0.1/images/8034_test_color.bmp', (imageData_0 / ratio))


# 展示图像
#cv2.imshow('img',imageData_0)
# 注意到这个函数只能显示uint8类型的数据，如果是uint16的数据请先转成uint8。否则图片显示会出现问题。**
#cv2.waitKey()
#cv2.destroyAllWindows()

