

class Rect():
    def __init__(self, cor_x_1, cor_y_1, cor_x_2, cor_y_2):
        self.x_1 = cor_x_1
        self.y_1 = cor_y_1
        self.x_2 = cor_x_2
        self.y_2 = cor_y_2
        self.width = self.x_2 - self.x_1
        self.height = self.y_2 - self.y_1

    def __repr__(self):
        return "{} {} - {} {}".format(
            self.x_1,
            self.y_1,
            self.x_2,
            self.y_2
        )

    def zoomRect(self):
        return Rect(
            self.x_1 + (0.25 * self.width),
            self.y_1 + (0.25 * self.height),
            self.x_1 + (0.75 * self.width),
            self.y_1 + (0.75 * self.height)
        )

    def leftRect(self):
        return Rect(
            self.x_1 - (0.25 * self.width),
            self.y_1,
            self.x_2 - (0.25 * self.width),
            self.y_2
        )

    def rightRect(self):
        return Rect(
            self.x_1 + (0.25 * self.width),
            self.y_1,
            self.x_2 + (0.25 * self.width),
            self.y_2
        )

    def upRect(self):
        return Rect(
            self.x_1,
            self.y_1 - (0.25 * self.height),
            self.x_2,
            self.y_2 - (0.25 * self.height)
        )

    def downRect(self):
        return Rect(
            self.x_1,
            self.y_1 + (0.25 * self.height),
            self.x_2,
            self.y_2 + (0.25 * self.height)
        )
