import pytest
import time

def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert soma(2, 2) == 4

@pytest.mark.rapido
def test_soma_rapida():
    assert soma(3, 3) == 6

@pytest.mark.lento
def test_multiplica_lenta():
    time.sleep(2)
    assert multiplica(3, 3) == 9

@pytest.mark.rapido
def test_multiplica_rapido():
    assert multiplica(4, 4) == 16