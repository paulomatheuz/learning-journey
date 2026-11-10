from basicos_03_pares import *


def test_eh_par():
    assert eh_par(10) == True
    assert eh_par(0) == True
    assert eh_par(5) == False
    assert eh_par(7) == False