from limites_01_meta import *


def test_atingiu_meta():
    assert atingiu_meta(99) == False
    assert atingiu_meta(100) == True
    assert atingiu_meta(101) == True