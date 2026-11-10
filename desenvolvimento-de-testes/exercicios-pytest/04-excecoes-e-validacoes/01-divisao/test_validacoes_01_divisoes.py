import pytest
from validacoes_01_divisao import *


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10,0)

def test_divisao_exata():
    resultado = dividir(10, 2)

    assert resultado == 5
    
    assert dividir(10, 5) == 2