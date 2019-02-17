
import math
import os
from colored import stylize, bg
from PIL import Image


def findNearestColor(color, pallette):
    distances = []
    (colorr, colorg, colorb) = color
    for c in pallette:
        (cr, cg, cb) = c
        distances.append(
            (colorr-cr)**2 +
            (colorg-cg)**2 +
            (colorb-cb)**2
        )
    return distances.index(min(distances))


def resize(imageName, basewidth, crop=(0,0,100,100)):
    img = Image.open(imageName) #.crop( crop )
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent))/2.0)
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # img.save(imageName+'.gif')
    return img


def getTerminalSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    r = int(rows)
    c = int(columns)
    return r, c


class Renderer(object):
    def __init__(self, colorPallette):
        self.colorPallette = colorPallette

    def render(self, fileName, width=None):
        if width == None:
            _, width = getTerminalSize()
        imgR = resize(fileName, width)
        imgX, imgY = imgR.size
        imageString = "\n"
        for j in range(imgY):
            for i in range(imgX):
                color = bg(findNearestColor(
                    imgR.getpixel((i, j)), self.colorPallette))
                imageString += stylize(" ", color)
            imageString += "\n"
        self.imageString = imageString
        return imageString

    def show(self, width=None):
        os.system("clear")
        print(self.imageString)
        result = ""
        while result != "q":
            result = raw_input("q for quit z for zoom: ")
            if result == "z":
                print("aaaaaaaaaaaaa")
