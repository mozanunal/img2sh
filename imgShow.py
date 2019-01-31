from __future__ import print_function
import colored
from colored import stylize
import os
from PIL import Image

def getTerminalSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    r = int(rows)
    c = int(columns)
    return r,c

def resizeAndSave(imageName, basewidth):
    img = Image.open(imageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent))/2.4)
    img = img.resize((basewidth,hsize),Image.ANTIALIAS).convert('P', palette=Image.WEB)
    img.save('sompic.gif')
    return img
    # print(img.getpixel((1, 2)))

def showImage(fileName):
    os.system("clear")
    termY,termX=getTerminalSize()
    imgR = resizeAndSave(fileName, termX-10)
    imgX,imgY = imgR.size

    for j in range( imgY ):
        for i in range( imgX ):
            print(
                stylize(
                    " ", 
                    colored.bg(
                        imgR.getpixel(
                            (i,j)
                        )
                    )
                    ),
                end=""
            )
        print()




if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        "-i","--image",
        help="image dir"
    )
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    args = parser.parse_args()

    showImage(args.image)





