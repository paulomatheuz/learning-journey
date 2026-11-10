import pytest
from validacoes_02_quantidade import *


def test_validar_quantidade_nao_inteiro():
    with pytest.raises(TypeError):
        validar_quantidade('10')

def test_validar_quantidade_negativa():
    with pytest.raises(ValueError):
        validar_quantidade(-10)

def test_validar_quantidade_zero():
    with pytest.raises(ValueError):
        validar_quantidade(0)

def test_validar_quantidade():
    assert validar_quantidade(2) == 2
    assert validar_quantidade(20) == 20
    assert validar_quantidade(200) == 200