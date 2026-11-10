from limites_03_faixas import *


def test_classificar_pontuação():
    assert classificar_pontuacao(49) == 'iniciante'

    assert classificar_pontuacao(50) == 'intermediario'
    assert classificar_pontuacao(79) == 'intermediario'
    
    assert classificar_pontuacao(80) == 'avancado'
    assert classificar_pontuacao(100) == 'avancado'