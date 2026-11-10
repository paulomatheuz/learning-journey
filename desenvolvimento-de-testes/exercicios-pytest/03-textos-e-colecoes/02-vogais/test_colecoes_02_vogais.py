from colecoes_02_vogais import *


def test_contar_vogais():
    assert contar_vogais('Se você não gosta do seu destino, não o aceite.') == 17
    assert contar_vogais('A força humana reside na capacidade de mudar a si mesmo.') == 22
    assert contar_vogais('Acredite no seu próprio poder.') == 11