from colecoes_05_agrupamento import *


def test_somar_por_categoria():
    itens = [
        {"categoria": "comida", "valor": 20},
        {"categoria": "bebida", "valor": 10},
        {"categoria": "comida", "valor": 30},
    ]

    esperado = {
        "comida": 50,
        "bebida": 10,
    }

    resultado = somar_por_categoria(itens)

    assert resultado == esperado