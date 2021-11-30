"""renderer module"""
import os
from six.moves import input
from colored import stylize, bg
from PIL import Image
import numpy as np

from .rect import Rect


def find_nearest_color(color, pallette):
    if len(color) == 3:
        (colorr, colorg, colorb) = color
    elif len(color) == 4:
        (colorr, colorg, colorb, alpha) = color
        if alpha == 0:
            return None  # pallette.index((255,255,255))
    colors = (colorr, colorg, colorb)
    diff = pallette - colors
    diff_sum = np.sum(np.square(diff), axis=1)
    return np.argmin(diff_sum)


def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)


class Renderer():
    """Renderer class which render images
    according to the specified color pallette
    """
    FONT_RATIO = 2.0
    ERROR_IMAGE_READ = 0
    ERROR_RENDER = 1

    def __init__(self, file_name, color_pallette, wsize=None):
        self.error = None
        if wsize is None:
            _, wsize = get_terminal_size()
        try:
            self.img = Image.open(file_name)
            self.wsize = wsize
            self.color_pallette = color_pallette
            self.render_count = 0
            self.img_x, self.img_y = self.img.size
            # no crop at the beginning
            self.crop = Rect(0, 0, self.img_x, self.img_y)
        except:
            print("ERROR: Image read")
            self.error = self.ERROR_IMAGE_READ

    def render(self, crop=None):
        """render the image

        Args:
            crop (Rect, optional): crop image according to the given rect. Defaults to None.

        Returns:
            str: the result string
        """
        self.render_count += 1
        img_r = self.img
        if crop is not None:
            self.crop = crop
            img_r = img_r.crop((crop.x1, crop.y1, crop.x2, crop.y2))
        img_rx, img_ry = img_r.size
        wpercent = (self.wsize/float(img_rx))
        hsize = int((float(img_ry)*float(wpercent))/self.FONT_RATIO)
        img_r = img_r.resize((self.wsize, hsize), Image.ANTIALIAS)
        self._convert_string(img_r)
        return self.image_string

    def show(self, interactive=False):
        """clear the screen and renders the image

        Args:
            interactive (bool, optional): is interactive. Defaults to False.
        """
        os.system("clear")
        print(self.image_string)
        print("[Crop]: ", self.crop)
        if interactive:
            self._interactive()

    def _convert_string(self, img_r):
        img_x, img_y = img_r.size
        image_string = "\n"
        for j in range(img_y):
            for i in range(img_x):
                color = find_nearest_color(
                    img_r.getpixel((i, j)), self.color_pallette)
                if color is None:
                    image_string += " "
                else:
                    color_value = bg(color)
                    image_string += stylize(" ", color_value)
            image_string += "\n"
        self.image_string = image_string

    def _interactive(self):
        cmd = input(
            "q: quit z: zoom+ x: zoom- c: reset \narrow keys for navigation \ncmd: ")
        if cmd == "q":
            return
        if cmd == "z":
            self.render(
                crop=self.crop.zoom_rect()
            )
        elif cmd == "x":
            self.render(
                crop=Rect(0, 0, self.img_x, self.img_y)
            )
        elif cmd == "c":
            self.render(
                crop=Rect(0, 0, self.img_x, self.img_y)
            )
        elif cmd == '\x1b[A':  # up
            self.render(crop=self.crop.up_rect())
        elif cmd == '\x1b[B':  # down
            self.render(crop=self.crop.down_rect())
        elif cmd == '\x1b[C':  # right
            self.render(crop=self.crop.right_rect())
        elif cmd == '\x1b[D':  # left
            self.render(crop=self.crop.left_rect())
        else:
            print("Unkown", cmd)
        self.show(interactive=True)
        # print(self.render_count)
