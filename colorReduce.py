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

# load reference color palette
refPal = iio.imread('referencePalette.png')

outImg = np.empty_like(img)

def euklideanDist(p1, p2):
    x = int(p1[0]) - int(p2[0])
    y = int(p1[1]) - int(p2[1])
    z = int(p1[2]) - int(p2[2])
    return np.sqrt(x**2+y**2+z**2)

def colorMapping(sampleColor):
    r = sampleColor[0]
    g = sampleColor[1]
    b = sampleColor[2]
    avgVal = np.average(sampleColor[:3])
    numGreys = 3
    step = 225/(numGreys-1)
    medianVals = [0] * numGreys
    for i in range(numGreys):
        medianVals[i] = 30 + i * step
    median = medianVals[int((avgVal+step/2)/step)] 
    greyScaleVal = [median, median, median, 255]
    outColor = greyScaleVal # grey as default
    dist = euklideanDist(sampleColor, greyScaleVal)
    for color in refPal[0] :
        newDist = euklideanDist(sampleColor, color)
        if newDist < dist:
            dist = newDist
            outColor = color
    return outColor

for row in range(height):
    for col in range(width):
        outImg[row][col] = colorMapping(img[row][col])

# output the image with reduced colors
iio.imwrite('img/output.png', outImg)