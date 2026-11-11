import pytest
from classifica_idade import classifica_idade

@pytest.mark.parametrize("idade, categoria_esperada", [
    (11, "Criança"), 
    (17, "Adolescente"), 
    (25, "Adulto"), 
    (60, "Idoso")
    ])
def test_classifica_idade(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada
