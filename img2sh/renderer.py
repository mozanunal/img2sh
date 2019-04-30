
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


def getTerminalSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    r = int(rows)
    c = int(columns)
    return r, c


class Renderer(object):
    FONT_RATIO = 2.0
    ERROR_IMAGE_READ = 0
    ERROR_RENDER = 1
    def __init__(self, fileName, colorPallette, wsize=None):
        self.error = None
        if wsize == None:
            _, wsize = getTerminalSize()
        try:
            self.img = Image.open(fileName)
        except:
            print( "ERROR: Image read" )
            self.error = self.ERROR_IMAGE_READ
        self.wsize = wsize
        self.colorPallette = colorPallette

    def render(self, crop=None):
        imgR = self.img
        if crop != None:
            imgR = imgR.crop(crop)
        imgRX, imgRY = imgR.size
        wpercent = (self.wsize/float(imgRX))
        hsize = int((float(imgRY)*float(wpercent))/self.FONT_RATIO)
        imgR = imgR.resize((self.wsize, hsize), Image.ANTIALIAS)
        self._convertString(imgR)
        return True

    def show(self, interactive=False):
        os.system("clear")
        print(self.imageString)
        if interactive:
            self._interactive()
    
    def _convertString(self, imgR):
        imgX, imgY = imgR.size
        imageString = "\n"
        for j in range(imgY):
            for i in range(imgX):
                color = bg(findNearestColor(
                    imgR.getpixel((i, j)), self.colorPallette))
                imageString += stylize(" ", color)
            imageString += "\n"
        self.imageString = imageString

    def _interactive(self):
        cmd = ""
        while cmd != "q":
            cmd = raw_input("q for quit z for zoom: ")
            if cmd == "z":
                self.render(crop=(0,0,100,100))
                self.show()
                print("aaaaaaaaaaaaa")
