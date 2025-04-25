import imageio.v3 as iio
import numpy as np
import sys

if len(sys.argv) > 2:
    print("Too many arguments, try again.\nYou should only put how many colors you want your palette to have.")
elif int(sys.argv[1]) < 5:
    print("You have to specify at least 5 colors.\nTry again.")
else:
    numColors = int(sys.argv[1])
    colors = np.zeros((1, numColors, 4),dtype=np.uint8) # all pixels blank
    colors[0][numColors-1] = [0, 0, 0, 255] # set last pixel white
    colors[0][numColors-2] = [255, 255, 255, 255] # set next to last pixel black
    rest = numColors - 2
    for row in range(1):
        for column in range(rest): # for the rest of the pixels get colors
            if (rest <= 3):
                h = 360 * column/rest # get hue as angle between 0 and 360 deg
                # s and v are 100% for now
                v = 1.0
                s = 1.0
            else:
                if (rest % 3 == 0): #number of remaining colors divisible by 3
                    h = 360 * 3*int(column/3)/rest # get hue as angle between 0 and 360 deg
                    if (column % 3  == 0):
                        s = 0.5
                        v = 1.0
                    elif (column % 3 == 1):
                        s = 1.0
                        v = 1.0
                    else:
                        s = 1.0
                        v = 0.5
                elif (rest % 2 == 0): # number of remaining colors divisible by 2
                    h = 360 * 2*int(column/2)/rest # get hue as angle between 0 and 360 deg
                    if (column % 2 == 0):
                        s = 0.75
                        v = 1.0
                    else:
                        s = 1.0
                        v = 0.75
                else:
                    h = 360 * column / numColors # get hue as angle between 0 and 360 deg
                    # s and v are 100% for now
                    v = 1.0
                    s = 1.0

            # calculate placeholders
            c = v * s
            x = c * (1 - np.abs((h/60)%2 - 1))
            m = v - c
            col = [0.0, 0.0, 0.0]
            if h >= 0 and h < 60:
                col = [c, x, 0]
            elif h >= 60 and h < 120:
                col = [x, c, 0]
            elif h >= 120 and h < 180:
                col = [0, c, x]
            elif h >= 180 and h < 240:
                col = [0, x, c]
            elif h >= 240 and h < 300:
                col = [x, 0, c]
            elif h >= 300 and h < 360:
                col = [c, 0, x]
            else:
                print("Error, invalid angle detected")
            colorRGB = [int((col[0]+m)*255), int((col[1]+m)*255), int((col[2]+m)*255), 255]
            print([h, s, v])
            colors[row][column] = colorRGB
    # write result into outputImg
    fileName = "FullSatHSVRefPal" + str(numColors) + ".png"
    iio.imwrite(fileName, colors)
    