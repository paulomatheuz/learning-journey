import pytest


def soma_dobro(numbers):
    return sum(x * 2 for x in numbers)


@pytest.fixture
def list_numbers():
    return [1, 2, 3, 4, 5]

def test_soma_dobro(list_numbers):
    resultado = soma_dobro(list_numbers)
    assert resultado == 30, "A soma do dobro dos números deve ser 30"

def test_soma_dobro_lista_vazia(list_numbers):
    list_numbers.clear()
    resultado = soma_dobro(list_numbers)
    assert resultado == 0, "A soma dos números deve ser 0"