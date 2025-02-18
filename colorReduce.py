import imageio.v3 as iio
import numpy as np


img = iio.imread('img/test.png')

height = img.shape[0]
width = img.shape[1]

# load reference color palette
refPal = iio.imread('referencePalette.png')

outImg = np.empty_like(img)


# output the image with reduced colors
iio.imwrite('img/output.png', outImg)