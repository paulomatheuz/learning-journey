from colecoes_04_filtragem import filtrar_pares


def test_filtrar_pares():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    esperado = [2, 4, 6, 8, 10]

    numero = filtrar_pares(numeros)

    assert numero == esperado