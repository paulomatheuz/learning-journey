from basicos_01_soma import *

def test_somar():
    assert somar(1, 2) == 3
    assert somar(-1, 3) == 2
    assert somar(10, -9) == 1