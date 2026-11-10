from basicos_04_saudacao import *


def test_criar_saudacao():
    assert criar_saudacao('paulo') == f'Olá, paulo!'
    assert criar_saudacao('pablo') == f'Olá, pablo!'
    assert criar_saudacao('nathalia') == f'Olá, nathalia!'