from basicos_05_media import *


def test_media_de_tres():
    assert media_de_tres(1, 2, 3) == 2
    assert media_de_tres(5, 10, 15) == 10
    assert media_de_tres(20, 40, 60) == 40