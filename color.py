import math

def findNearestColor(color, pallette):
    distances = []
    (colorr,colorg,colorb) = color
    for c in pallette:
        (cr,cg,cb) = c
        distances.append(
            (colorr-cr)**2 +
            (colorg-cg)**2 +
            (colorb-cb)**2
        )
    return distances.index(min(distances))
