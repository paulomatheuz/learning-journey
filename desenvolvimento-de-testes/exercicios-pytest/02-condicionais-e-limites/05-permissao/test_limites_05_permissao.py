from limites_05_permissao import *


def test_pode_acessar():
    assert pode_acessar(True, False, True) == True

    assert pode_acessar(True, True, True) == False
    assert pode_acessar(True, False, False) == False
    assert pode_acessar(False, False, True) == False
    
    assert pode_acessar(False, False, False) == False
