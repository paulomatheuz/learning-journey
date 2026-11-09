def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([10, 20, 30]) == 60
    assert sum([13, 6, 7]) == 26

def test_len():
    assert len([10, 20, 30]) == 3
    assert len("Python") == 6
    assert len([]) == 0

def multiplicar(a, b):
    return a * b

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10
    assert multiplicar(7, 0) == 0