

class Rect(object):
    def __init__(self, corX1, corY1, corX2, corY2):
        self.x1 = corX1
        self.y1 = corY1
        self.x2 = corX2
        self.y2 = corY2
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1

    def __repr__(self):
        return "{} {} - {} {}".format(
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )

    def zoomRect(self):
        return Rect(
            self.x1 + ( 0.25 * self.width),
            self.y1 + ( 0.25 * self.height),
            self.x1 + ( 0.75 * self.width),
            self.y1 + ( 0.75 * self.height)
        )

    def leftRect(self):
        return Rect(
            self.x1 - ( 0.25 * self.width),
            self.y1,
            self.x2 - ( 0.25 * self.width),
            self.y2
        )

    def rightRect(self):
        return Rect(
            self.x1 + ( 0.25 * self.width),
            self.y1,
            self.x2 + ( 0.25 * self.width),
            self.y2
        )

    def upRect(self):
        return Rect(
            self.x1,
            self.y1 - ( 0.25 * self.height),
            self.x2,
            self.y2 - ( 0.25 * self.height)
        )

    def downRect(self):
        return Rect(
            self.x1,
            self.y1 + ( 0.25 * self.height),
            self.x2,
            self.y2 + ( 0.25 * self.height)
        )