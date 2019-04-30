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
    parser.add_argument(
        "-i", "--interactive",
        help="Open image in interactive mode",
        type=bool
    )

    args = parser.parse_args()

    r = Renderer(args.Image, XTERM_PALLETTE, wsize=args.width)
    if r.error==None:
        r.render()
        r.show(interactive=args.interactive)

if __name__ == "__main__":
    main()
