from funcoes import *

def test_email_valido():
    assert email_valido("exemplo.com") is False
    assert email_valido("paulomatheuz.email@gmail.com") is True

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(10, 0) is None