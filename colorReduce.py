import imageio.v3 as iio
import numpy as np
from enum import Enum

img = iio.imread('img/testw100.png')
prev = iio.imread('img/output.png')

rows = img.shape[0]
cols = img.shape[1]

# load reference color palette
refPal = iio.imread('FullSatHSVRefPal24.png')
colors = refPal.shape[1]

#outImg = np.empty((rows, cols, 4),dtype=np.uint8)
outImg = np.copy(prev)
satPal = np.empty((1, int(colors/2), 4),dtype=np.uint8)
unSatPal = np.empty((1, int(colors/2), 4),dtype=np.uint8)

def getColorVector(sample):
    rVec = sample[0] - 128
    gVec = sample[1] - 128
    bVec = sample[2] - 128
    return [rVec, gVec, bVec]


def euklideanDist(p1, p2):
    x = int(p1[0]) - int(p2[0])
    y = int(p1[1]) - int(p2[1])
    z = int(p1[2]) - int(p2[2])
    return np.sqrt(x**2+y**2+z**2)

# calculate dot product of two 3D-vectors
def dotProd(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

# calculate length of a 3D vector normalized for the scope of the color space (furthest is 100)
def vecLen(v):
    return np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

# calculates the angle between two vectors in degrees
def calcAngleTweenVec(v1, v2):
    lenProd = vecLen(v1) * vecLen(v2)
    if lenProd == 0: # comparison with origin
        return 180.0 # yields maximum angle otherwise later division by zero
    blep = dotProd(v1, v2) / lenProd
    eps = 0.0000001
    if np.abs(blep) > 1:
        if np.abs(blep)-1 < eps:
            blep = np.sign(blep) * 1.0
        else:
            print("Error, arccos input out of scope", blep)
    angle = 180*(np.arccos(blep))/np.pi
    return angle

lengths = []
for c in refPal[0]:
    lgth = vecLen(getColorVector(c))/np.sqrt(3*128**2)
    lengths.append(lgth)
lengths.sort()
medLen = lengths[int(len(lengths)/2)]

sat = 0
unsat = 0
for clr in range(colors):
    lgth = vecLen(getColorVector(refPal[0][clr]))/np.sqrt(3*128**2)
    if lgth >= medLen:
        satPal[0][sat] = refPal[0][clr]
        sat += 1
    elif lgth < medLen:
        unSatPal[0][unsat] = refPal[0][clr]
        unsat += 1
    else:
        print("Whaaaaa")

print(satPal)
print(unSatPal)
print(medLen)

def colorMapping(sampleColor):
    r = sampleColor[0]
    g = sampleColor[1]
    b = sampleColor[2]
    a = 255
    outColor = [r, g, b, a]
    angle = 180
    sampleVec = getColorVector(sampleColor) 
    dist = vecLen(sampleVec) # distance of sample from grey
    maxDist = np.sqrt(3*128**2) # maximum distance of a color in given space from center
    normedVecLen = dist/maxDist
    for color in refPal[0] :
        palVec = getColorVector(color)
        newAngle = calcAngleTweenVec(palVec, sampleVec)
        if normedVecLen < 0.1: # everything close to center gets mapped to grey
            outColor = [128, 128, 128, 255]
            angle = 0
        if newAngle < angle:
            angle = newAngle
            outColor = color
        #newDist = euklideanDist(sampleColor[:3], color[:3])
        #if newDist < dist:
        #    dist = newDist
        #    outColor = color
    if angle == 180: # something wrong, because max angle matched
        print(sampleVec, " This vector makes a weird angle")
    return outColor

for row in range(int(rows)):
    for col in range(int(cols)):
        mappedColor = colorMapping(img[row][col])
        outImg[row][col] = mappedColor
        if (row % 50 == 0 and col == 0):
            iio.imwrite('img/output.png', outImg)
            gap = ""
            if (row/rows) < 0.1:
                gap = "  "
            elif (row/rows) < 1.0:
                gap = " "
            print("Progress: " + gap + str(int(10000*row/rows)/100) + "%  ", end='\r')

# output the image with reduced colors
iio.imwrite('img/output.png', outImg)