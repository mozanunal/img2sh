#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import colored
from colored import stylize
from PIL import Image
from xtermColor import xtermPallette
from color import findNearestColor

def getTerminalSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    r = int(rows)
    c = int(columns)
    return r,c

def resizeAndSave(imageName, basewidth):
    img = Image.open(imageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent))/2.0)
    img = img.resize((basewidth,hsize),Image.ANTIALIAS)
    img.save(imageName+'.gif')
    return img
    # print(img.getpixel((1, 2)))

def renderImage(fileName, pallette):
    termY,termX=getTerminalSize()
    imgR = resizeAndSave(fileName, termX)
    imgX,imgY = imgR.size
    imageString = "\n"
    for j in range( imgY ):
        for i in range( imgX ):
            color = colored.bg( findNearestColor( imgR.getpixel((i,j)), pallette ) )
            imageString+= stylize( " ", color )
        imageString+="\n"
    return imageString




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        "-i","--image",
        help="image dir"
    )

    args = parser.parse_args()
    
    XTermPallette = xtermPallette()

    os.system("clear")

    termImage = renderImage(args.image, XTermPallette)
    print(termImage)
    #print(XTermPallette)





