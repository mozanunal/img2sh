"""rectangle module extended for navigation functions"""


class Rect():
    """Rectangle helper class
    """

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

    def zoom_rect(self):
        """zoom_rect

        Returns:
            Rect: mid zoomed rect
        """
        return Rect(
            self.x_1 + (0.25 * self.width),
            self.y_1 + (0.25 * self.height),
            self.x_1 + (0.75 * self.width),
            self.y_1 + (0.75 * self.height)
        )

    def left_rect(self):
        """left_rect

        Returns:
            Rect: left rectangle
        """
        return Rect(
            self.x_1 - (0.25 * self.width),
            self.y_1,
            self.x_2 - (0.25 * self.width),
            self.y_2
        )

    def right_rect(self):
        """right_rect

        Returns:
            Rect: right rectangle
        """
        return Rect(
            self.x_1 + (0.25 * self.width),
            self.y_1,
            self.x_2 + (0.25 * self.width),
            self.y_2
        )

    def up_rect(self):
        """up_rect

        Returns:
            Rect: up rectangle
        """
        return Rect(
            self.x_1,
            self.y_1 - (0.25 * self.height),
            self.x_2,
            self.y_2 - (0.25 * self.height)
        )

    def down_rect(self):
        """down_rect

        Returns:
            Rect: down rectangle
        """
        return Rect(
            self.x_1,
            self.y_1 + (0.25 * self.height),
            self.x_2,
            self.y_2 + (0.25 * self.height)
        )
