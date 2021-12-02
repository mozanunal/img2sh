"""cli module for img2sh"""
from __future__ import print_function
from .renderer import Renderer
from .pallette import XTERM_PALLETTE


def is_link(test_string):
    """check if the string is a web link

    Args:
        test_string (str): input string

    Returns:
        bool: if string is an http link
    """
    return test_string.startswith('http')


def main():
    """main cli function
    """
    import argparse

    parser = argparse.ArgumentParser(
        description='Show images directly on terminal.')
    parser.add_argument(
        "Image", help="the directory of the image which will be opened")
    parser.add_argument(
        "-w", "--width",
        help="image width on the terminal",
        type=int
    )
    parser.add_argument(
        "-i", "--interactive",
        default=False, action='store_true',
        help="open image in interactive mode",
    )

    args = parser.parse_args()

    renderer = Renderer(args.Image, XTERM_PALLETTE, wsize=args.width)
    if renderer.error is None:
        renderer.render()
        renderer.show(interactive=args.interactive)


if __name__ == "__main__":
    main()
