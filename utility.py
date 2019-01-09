# =============================================================
# This file contains helper functions and classes
#
# Mushfiqul Alam, 2017
#
# Report bugs/suggestions:
#   mushfiqulalam@gmail.com
# =============================================================

import png
import numpy as np
import scipy.misc
import math
from scipy import signal        # for convolutions
from scipy import ndimage       # for n-dimensional convolution
from scipy import interpolate


# =============================================================
# function: readRawData
#   basic process raw image data
#   data:   is the image data
#   output_bits: output data bits
#   input_bits: input data bits
#   input_format: bayer pattern, or 4c pattern
#   input_width, input_height : image size
# =============================================================
def readRawData(image_name, input_bits, input_format, input_width, input_height):

    if input_bits == 8 :
        type1 = 'uint8'
    else:
        type1 = 'uint16'
   
    width = input_width
    height = input_height
    imgData = np.fromfile(image_name, dtype=type1)
    imgData = imgData.reshape(height,width)
    
    full_size_3channels = np.empty((height, width, 3), dtype=type1)
    data_4chennels = np.empty((int(height/2), int(width/2), 4), dtype=type1)

    if input_format == 'rggb':
        r_channel = imgData[::2,::2]
        gr_channel = imgData[::2,1::2]
        b_channel = imgData[1::2,1::2]
        gb_channel = imgData[1::2,::2]


    elif input_format == 'bggr':
        r_channel = imgData[1::2,1::2]
        gr_channel = imgData[1::2,::2]
        b_channel = imgData[::2,::2]
        gb_channel = imgData[::2,1::2]

    elif input_format == 'grbg':
        r_channel = imgData[::2,1::2]
        gr_channel = imgData[::2,::2]
        b_channel = imgData[1::2,::2]
        gb_channel = imgData[1::2,1::2]


    elif input_format == 'gbrg':
        r_channel = imgData[1::2,::2]
        gr_channel = imgData[1::2,1::2]
        b_channel = imgData[::2,1::2]
        gb_channel = imgData[::2,::2]


    else:
        print('sorry! no match fomat')


    full_size_3channels[::2, ::2, 2] = r_channel
    full_size_3channels[::2, 1::2, 1] = gr_channel
    full_size_3channels[1::2, 1::2, 0] = b_channel
    full_size_3channels[1::2, ::2, 1] = gb_channel

    data_4chennels[:, :, 0] = r_channel
    data_4chennels[:, :, 1] = gr_channel
    data_4chennels[:, :, 2] = gb_channel
    data_4chennels[:, :, 3] = b_channel
    return full_size_3channels, data_4chennels
