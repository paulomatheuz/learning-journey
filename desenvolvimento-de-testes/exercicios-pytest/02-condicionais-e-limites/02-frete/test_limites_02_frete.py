from limites_02_frete import *


def test_calcular_frete():
    assert calcular_frete(199, True) == 0

    assert calcular_frete(199, False) == 15
    assert calcular_frete(200, False) == 0
    assert calcular_frete(201, False) == 0