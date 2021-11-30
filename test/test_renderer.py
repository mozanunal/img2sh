
from img2sh.renderer import Renderer
from img2sh.pallette import XTERM_PALLETTE


def test_jpeg():
    renderer = Renderer("examples/chrome.jpeg", XTERM_PALLETTE, wsize=80)
    assert renderer.error is None
    result_img = renderer.render()
    f_true = open("examples/chrome.jpeg.bin", "r+")
    f_false = open("examples/chrome.png.bin", "r+")
    assert result_img is not None
    assert len(result_img) == 48168
    assert f_true.read() == result_img
    assert f_false.read() != result_img


def test_png():
    renderer = Renderer("examples/chrome.png", XTERM_PALLETTE, wsize=80)
    assert renderer.error is None
    result_img = renderer.render()
    f_true = open("examples/chrome.png.bin", "r+")
    f_false = open("examples/chrome.jpeg.bin", "r+")
    assert result_img is not None
    assert len(result_img) == 39780
    assert f_true.read() == result_img
    assert f_false.read() != result_img
