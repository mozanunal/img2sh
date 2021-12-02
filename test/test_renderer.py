
from numpy import e
from img2sh.renderer import Renderer
from img2sh.pallette import XTERM_PALLETTE

def test_jpeg():
    renderer = Renderer("examples/lena.jpeg", XTERM_PALLETTE, wsize=80)
    assert renderer.error is None
    result_img = renderer.render()
    expected_wsize = 80
    expected_hsize = expected_wsize / 2
    expected_len = (expected_wsize * expected_hsize) + expected_hsize + 1

    assert renderer.wsize == 80
    assert result_img.count("\n") == (expected_hsize+1)
    assert result_img is not None
    assert len(result_img) == expected_len


def test_png():
    renderer = Renderer("examples/terminal.png", XTERM_PALLETTE, wsize=80)
    assert renderer.error is None
    result_img = renderer.render()
    expected_wsize = 80
    expected_hsize = int(expected_wsize / 2)
    expected_len = (expected_wsize * expected_hsize) + expected_hsize + 1

    assert renderer.wsize == 80
    assert result_img.count("\n") == (expected_hsize+1)
    assert result_img is not None
    assert len(result_img) == expected_len
