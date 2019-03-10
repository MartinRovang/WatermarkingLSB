############################################################
#                                                          #
#                Made by Martin Soria Røvang               #
#              Github: github.com/martinrovang             #
#                                                          #
############################################################


import numpy as np 
import matplotlib.pyplot as plt
import sys

# Get info
flag = sys.argv[1]

if flag == '-e':
    extractim_path = sys.argv[2]
    # loading png yield float array therefore multiply by 255 to get integer intensity values
    extractim = plt.imread(extractim_path)*255
    extractim = extractim.astype('uint8')
    if len(sys.argv) > 3:
        raise Exception('You are using wrong arguments, extraction only takes 1 argument(image)')


if flag == '-w':
    originalim_path = sys.argv[2]
    image = plt.imread(originalim_path)
    image.setflags(write=1)
    image = image.astype('uint8')
    w_path = sys.argv[3]
    watermark = plt.imread(w_path)
    wtemp = np.zeros(image.shape)
    wtemp[0:watermark.shape[0], 0:watermark.shape[1]] = watermark
    # Make sure they are uint8
    wtemp = wtemp.astype('uint8')


def watermark(x, w):
    """Watermarks the image by replacing the least significant bits of the image."""
    x = format(x, '#010b')
    w = format(w, '#010b')
    toadd = w[2:4]
    temp = x[:-2] + toadd
    result = int(temp, 2)
    return result


def dewatermark(x):
    """Removes all the significant bits and place the least significant bits to the most significant for watermark extraction."""
    x = format(x, '#010b')
    first = '0b'
    mid = x[-2:]
    third = '000000'
    y = first + mid + third
    result = int(y, 2)
    return result

# Vectorize the functions
vecwatermark = np.vectorize(watermark)
vecdewatermark = np.vectorize(dewatermark)

# If watermark flag, add watermark to image.
if flag == '-w':
    print('Watermarking image...')
    watermarked = vecwatermark(image, wtemp)
    plt.figure()
    plt.axis('off')
    plt.imshow(watermarked)
    plt.savefig('Watermarkedimage.png', bbox_inches='tight', transparent=True, pad_inches=0)
    plt.close()
    print('Watermarking Complete')
    print('Saved as Watermarkedimage.png')

if flag == '-e':
    print('Extracting image...')
    dewatermarked = vecdewatermark(extractim)
    print(np.unique(dewatermarked))
    plt.figure()
    plt.axis('off')
    plt.imshow(dewatermarked)
    plt.savefig('extractedwatermark.png', bbox_inches='tight', transparent=True, pad_inches=0)
    plt.close()
    print('Extracting Complete')
    print('Saved as extractedwatermark.png')


