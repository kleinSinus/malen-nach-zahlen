# Color Mapper v 0.1
#
# author: Wilhelm Simus
# 
# This tool takes an input image and a color palette and reduces the image to only colors of said
# palette. The output gets written into its own image file in the same location as the input image.
# 
# Input arguments:
# - file location relative to this script
# - file location for the color palette (optional)
# - used measurement of color distance (optional)

import imageio.v3 as iio
import numpy as np
import sys
from enum import Enum

# Load an image. If none specified, load test image as fallback.
if len(sys.argv) <= 1: # if no arguments are given present instructions
    print("No argument specified. You need to at least specify an input file.\n" +
          "The input arguments are:\n" +
          "1. Input File (specify using file location relative to this script)\n" +
          "2. Color Palette (optional argument for when you want to provide a 2nd image with a\n" +
          "                  color palette, note that the script expects images with only one\n" +
          "                  row of pixels. If you provide any picture, only the first row\n" +
          "                  will be evaluated as palette.)\n" +
          "   Alternatively you can provide the number of colors the image should be reduced\n" +
          "   to and a palette will be generated.\n" +
          "3. Similarity Measurement (There's different ways to measure distance between \n"  +
          "                           colors and what might be computationally intuitive does\n" +
          "                           not necessarily match human's intuitions about color\n"+
          "                           similarity)\n"+
          "   Available options are:\n" +
          "   - ANGRGB: Angular distance in a cube-shaped RGB-Color-Space with origin in\n" +
          "             RGB(0.5,0.5,0.5)\n" +
          "   - EUKRGB: Euklidean distance in a cube-shaped RGB-Color-Space\n" +
          "   - EUKHSV: Euklidean distance in a cylinder shaped HSV-Color-Space\n" +
          "   - ... other possible measurements might be implemented\n"+
          "\n"+
          "Example uses:\n"
          "    colorMapper img/test.png\n" + 
          "    colorMapper img/test.png 16\n" + 
          "    colorMapper img/test.png palette/Watercolor.png\n" + 
          "    colorMapper img/test.png 16 EUKRGB")
elif len(sys.argv) > 4:
    print("Too many arguments provided. Please stick to the predefined input arguments.\n" +
          "The input arguments are:\n" +
          "1. Input File (specify using file location relative to this script)\n" +
          "2. Color Palette (optional argument for when you want to provide a 2nd image with a\n" +
          "                  color palette, note that the script expects images with only one\n" +
          "                  row of pixels. If you provide any picture, only the first row\n" +
          "                  will be evaluated as palette.)\n" +
          "   Alternatively you can provide the number of colors the image should be reduced\n" +
          "   to and a palette will be generated.\n" +
          "3. Similarity Measurement (There's different ways to measure distance between \n"  +
          "                           colors and what might be computationally intuitive does\n" +
          "                           not necessarily match human's intuitions about color\n"+
          "                           similarity)\n"+
          "   Available options are:\n" +
          "   - ANGRGB: Angular distance in a cube-shaped RGB-Color-Space with origin in\n" +
          "             RGB(0.5,0.5,0.5)\n" +
          "   - EUKRGB: Euklidean distance in a cube-shaped RGB-Color-Space\n" +
          "   - EUKHSV: Euklidean distance in a cylinder shaped HSV-Color-Space\n" +
          "   - ... other possible measurements might be implemented"+
          "\n"+
          "Example uses:\n"
          "    colorMapper img/test.png\n" + 
          "    colorMapper img/test.png 16\n" + 
          "    colorMapper img/test.png palette/Watercolor.png\n" + 
          "    colorMapper img/test.png 16 EUKRGB")

else:
    fileName = 'img/testw100.png'
    img = iio.imread(fileName)
    iio.imwrite("img/testw100_copy.png", img)