
import math
import os
from six.moves import input
from rect import Rect
from colored import stylize, bg
from PIL import Image


def findNearestColor(color, pallette):
    distances = []
    if len(color) == 3:
        (colorr, colorg, colorb) = color
    elif len(color) == 4:
        (colorr, colorg, colorb, alpha) = color
        if alpha == 0:
            return None  # pallette.index((255,255,255))
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
            self.wsize = wsize
            self.colorPallette = colorPallette
            self.renderCount = 0
            self.imgX, self.imgY = self.img.size
            # no crop at the beginning
            self.crop = Rect(0, 0, self.imgX, self.imgY)
        except:
            print("ERROR: Image read")
            self.error = self.ERROR_IMAGE_READ

    def render(self, crop=None):
        self.renderCount += 1
        imgR = self.img
        if crop != None:
            self.crop = crop
            imgR = imgR.crop((crop.x1, crop.y1, crop.x2, crop.y2))
        imgRX, imgRY = imgR.size
        wpercent = (self.wsize/float(imgRX))
        hsize = int((float(imgRY)*float(wpercent))/self.FONT_RATIO)
        imgR = imgR.resize((self.wsize, hsize), Image.ANTIALIAS)
        self._convertString(imgR)
        return True

    def show(self, interactive=False):
        os.system("clear")
        print(self.imageString)
        print("Crop: ", self.crop)
        if interactive:
            self._interactive()

    def _convertString(self, imgR):
        imgX, imgY = imgR.size
        imageString = "\n"
        for j in range(imgY):
            for i in range(imgX):
                color = findNearestColor(
                    imgR.getpixel((i, j)), self.colorPallette)
                if color == None:
                    imageString += " "
                else:
                    colorValue = bg(color)
                    imageString += stylize(" ", colorValue)
            imageString += "\n"
        self.imageString = imageString

    def _interactive(self):
        cmd = input("q: quit z: zoom+ x: zoom- c: reset \ncmd: ")
        if cmd == "q":
            return
        elif cmd == "z":
            self.render(
                crop=self.crop.zoomRect()
            )            
        elif cmd == "x":
            self.render(
                crop=Rect(0,0,self.imgX,self.imgY)
            )
        elif cmd == "c":
            self.render(
                crop=Rect(0,0,self.imgX,self.imgY)
            )
        elif cmd == '\x1b[A': # up
            self.render(crop=self.crop.upRect())
        elif cmd == '\x1b[B': # down
            self.render(crop=self.crop.downRect())
        elif cmd == '\x1b[C': # right
            self.render(crop=self.crop.rightRect())
        elif cmd == '\x1b[D': # left
            self.render(crop=self.crop.leftRect())
        else:
            print("Unkown", cmd)
        self.show(interactive=True)
        #print(self.renderCount)
