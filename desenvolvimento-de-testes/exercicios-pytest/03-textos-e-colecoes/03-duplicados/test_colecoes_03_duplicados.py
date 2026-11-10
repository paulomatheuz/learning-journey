from colecoes_03_duplicados import *


def test_remover_duplicados():
    numeros = [1, 2, 3, 3, 4, 5, 5, 6]
    esperado = [1, 2, 3, 4, 5, 6]

    resultado = remover_duplicados(numeros)

    assert resultado == esperado