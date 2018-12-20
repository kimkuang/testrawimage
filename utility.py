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
def readRawData(image_name, input_bits, input_format, input_width, input_height, output_bits):

    if input_bits == 8 :
        type1 = 'uint8'
    else:
        type1 = 'uint16'

    if output_bits == 8 :
        type2 = 'uint8'
    else:
        type2 = 'uint16'       

    imgData = np.fromfile(image_name, dtype=type1)

    width = input_width
    height = input_height

    full_size_3channels = np.zeros((height*width*3),dtype=type2)
    r_channel = np.zeros(int(width*height/4), dtype=type2)
    gr_channel = np.zeros(int(width*height/4), dtype=type2)
    gb_channel = np.zeros(int(width*height/4), dtype=type2)
    b_channel = np.zeros(int(width*height/4), dtype=type2)
    data_4chennels = np.zeros([int(width*height/4), 4], dtype=type2)

    i, j, k, m = 0, 0, 0, 0

    if input_format == 'rggb':
        while k < (height-1):
            n = k*width*3+width*3
            while i < n:
                full_size_3channels[i+2] = imgData[j]
                r_channel[m] = imgData[j]
                full_size_3channels[i+4] = imgData[j+1]
                gr_channel[m] = imgData[j+1]
                full_size_3channels[i+width*3+1] = imgData[j+width]
                gb_channel[m] = imgData[j+width]
                full_size_3channels[i+width*3+3] = imgData[j+1+width]
                b_channel[m] = imgData[j+1+width]
                i = i + 6
                j = j + 2
                m = m + 1
            j = j + width
            k = k + 2
            i = i + width*3
        
        r_channel
        gr_channel
        gb_channel
        b_channel

    elif input_format == 'bggr':
        while k < (height-1):
            n = k*width*3+width*3
            while i < n:
                full_size_3channels[i] = imgData[j]
                full_size_3channels[i+4] = imgData[j+1]
                full_size_3channels[i+width*3+1] = imgData[j+width]
                full_size_3channels[i+width*3+5] = imgData[j+1+width]
                i = i + 6
                j = j + 2
            j = j + width
            k = k + 2
            i = i + width*3

    elif input_format == 'grbg':
        while k < (height-1):
            n = k*width*3+width*3
            while i < n:
                full_size_3channels[i+1] = imgData[j]
                full_size_3channels[i+5] = imgData[j+1]
                full_size_3channels[i+width*3] = imgData[j+width]
                full_size_3channels[i+width*3+4] = imgData[j+1+width]
                i = i + 6
                j = j + 2
            j = j + width
            k = k + 2
            i = i + width*3   

    elif input_format == 'gbrg':
        while k < (height-1):
            n = k*width*3+width*3
            while i < n:
                full_size_3channels[i+1] = imgData[j]
                full_size_3channels[i+3] = imgData[j+1]
                full_size_3channels[i+width*3+2] = imgData[j+width]
                full_size_3channels[i+width*3+4] = imgData[j+1+width]
                i = i + 6
                j = j + 2
            j = j + width
            k = k + 2
            i = i + width*3 

    else:
        print('sorry! no match fomat')

    full_size_3channels = full_size_3channels.reshape(height, width, 3)
    data_4chennels[:,0] = r_channel
    data_4chennels[:,1] = gr_channel
    data_4chennels[:,2] = gb_channel
    data_4chennels[:,3] = b_channel
    return full_size_3channels, data_4chennels


''''
# =============================================================
# function: imsave
#   save image in image formats
#   data:   is the image data
#   output_dtype: output data type
#   input_dtype: input data type
#   is_scale: is scaling needed to go from input data type to output data type
# =============================================================
def imsave(data, output_name, output_dtype="uint8", input_dtype="uint8", is_scale=False):

    dtype_dictionary = {"uint8" : np.uint8(data), "uint16" : np.uint16(data),\
                        "uint32" : np.uint32(data), "uint64" : np.uint64(data),\
                        "int8" : np.int8(data), "int16" : np.int16(data),\
                        "int32" : np.int32(data), "int64" : np.int64(data),\
                        "float16" : np.float16(data), "float32" : np.float32(data),\
                        "float64" : np.float64(data)}

    min_val_dictionary = {"uint8" : 0, "uint16" : 0,\
                          "uint32" : 0, "uint64" : 0,\
                          "int8" : -128, "int16" : -32768,\
                          "int32" : -2147483648, "int64" : -9223372036854775808}

    max_val_dictionary = {"uint8" : 255, "uint16" : 65535,\
                          "uint32" : 4294967295, "uint64" : 18446744073709551615,\
                          "int8" : 127, "int16" : 32767,\
                          "int32" : 2147483647, "int64" : 9223372036854775807}

    # scale the data in case scaling is necessary to go from input_dtype
    # to output_dtype
    if (is_scale):

        # convert data into float32
        data = np.float32(data)

        # Get minimum and maximum value of the input and output data types
        in_min  = min_val_dictionary[input_dtype]
        in_max  = max_val_dictionary[input_dtype]
        out_min = min_val_dictionary[output_dtype]
        out_max = max_val_dictionary[output_dtype]

        # clip the input data in the input_dtype range
        data = np.clip(data, in_min, in_max)

        # scale the data
        data = out_min + (data - in_min) * (out_max - out_min) / (in_max - in_min)

        # clip scaled data in output_dtype range
        data = np.clip(data, out_min, out_max)

    # convert the data into the output_dtype
    data = dtype_dictionary[output_dtype]

    # output image type: raw, png, jpeg
    output_file_type = output_name[-3:]

    # save files depending on output_file_type
    if (output_file_type == "raw"):
        pass # will be added later
        return

    elif (output_file_type == "png"):

        # png will only save uint8 or uint16
        if ((output_dtype == "uint16") or (output_dtype == "uint8")):
            if (output_dtype == "uint16"):
                output_bitdepth = 16
            elif (output_dtype == "uint8"):
                output_bitdepth = 8

            pass
        else:
            print("For png output, output_dtype must be uint8 or uint16")
            return

        with open(output_name, "wb") as f:
            # rgb image
            if (np.ndim(data) == 3):
                # create the png writer
                writer = png.Writer(width=data.shape[1], height=data.shape[0],\
                                    bitdepth = output_bitdepth)
                # convert data to the python lists expected by the png Writer
                data2list = data.reshape(-1, data.shape[1]*data.shape[2]).tolist()
                # write in the file
                writer.write(f, data2list)

            # greyscale image
            elif (np.ndim(data) == 2):
                # create the png writer
                writer = png.Writer(width=data.shape[1], height=data.shape[0],\
                                    bitdepth = output_bitdepth,\
                                    greyscale = True)
                # convert data to the python lists expected by the png Writer
                data2list = data.tolist()
                # write in the file
                writer.write(f, data2list)

    elif (output_file_type == "jpg"):
        pass # will be added later
        return

    else:
        print("output_name should contain extensions of .raw, .png, or .jpg")
        return
'''