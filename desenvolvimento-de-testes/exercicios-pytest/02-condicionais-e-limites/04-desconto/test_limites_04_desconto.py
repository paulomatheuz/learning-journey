from limites_04_desconto import *


def test_percentual_desconto():
    assert percentual_desconto(99, True) == 20
    assert percentual_desconto(100, True) == 20
    assert percentual_desconto(101, True) == 20

    assert percentual_desconto(99, False) == 0
    assert percentual_desconto(100, False) == 10
    assert percentual_desconto(101, False) == 10
