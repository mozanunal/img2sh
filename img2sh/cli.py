#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from renderer import Renderer
from pallette import XTERM_PALLETTE, BINARY_PALLETTE


def isLink(test_string):
    return test_string.startswith('http')

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Show images directly on terminal.')
    parser.add_argument("Image")
    parser.add_argument(
        "-w", "--width",
        help="image width",
        type=int
    )

    args = parser.parse_args()

    r = Renderer(XTERM_PALLETTE)
    r.render(args.Image, width=args.width)
    r.show()

if __name__ == "__main__":
    main()
