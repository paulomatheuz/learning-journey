from colecoes_01_normalizacao import *


def test_normalizar_usuario():
    assert normalizar_usuario(' PaUlo ') == 'paulo'
    assert normalizar_usuario(' PAULO ') == 'paulo'
    assert normalizar_usuario('      PAUlo') == 'paulo'
    assert normalizar_usuario('      PauLO') == 'paulo'
    assert normalizar_usuario(' PAULo     ') == 'paulo'
    assert normalizar_usuario(' PauLO     ') == 'paulo'