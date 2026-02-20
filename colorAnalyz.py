import imageio.v3 as iio
import numpy as np
from enum import Enum

class Color(Enum):
    RED = 0
    GRN = 1
    BLU = 2

img = iio.imread('img/test.png')

height = img.shape[0]
width = img.shape[1]

colors = []

for color in img:
    colors.append(color)
    print(colors)

# output the image with reduced colors
iio.imwrite('img/output.png', outImg)