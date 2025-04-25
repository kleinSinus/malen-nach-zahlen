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
#    a = 255
    outColor = [sampleColor[0], sampleColor[1], sampleColor[2]]
    avgVal = np.average(sampleColor[:3])
    #print("sample: ", sampleColor)
    #print(avgVal)
    numGreys = 3
    step = 225/(numGreys-1)
    medianVals = [0] * numGreys
    for i in range(numGreys):
        medianVals[i] = 30 + i * step
    median = medianVals[int((avgVal+step/2)/step)] 
    greyScaleVal = [median, median, median]
    outColor = greyScaleVal # grey as default
    dist = euklideanDist(sampleColor, greyScaleVal)
    for color in refPal[0] :
        newDist = euklideanDist(sampleColor, color)
        if newDist < dist:
            dist = newDist
            outColor = color[:3]
    return outColor

for row in range(int(height)):
    for col in range(int(width)):
        #print(row, col)
        mappedColor = colorMapping(img[row][col])
        #print(mappedColor)
        outImg[row][col] = mappedColor
        iio.imwrite('img/output.png', outImg)

# output the image with reduced colors
iio.imwrite('img/output.png', outImg)