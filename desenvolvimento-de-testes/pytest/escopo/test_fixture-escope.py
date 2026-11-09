import pytest

@pytest.fixture(scope="function") #durante um único teste. teardown após terminar.
def fixture_function():
    return 10

@pytest.fixture(scope="module") #entre os testes de uma classe. teardown após teste dessa classe.
def fixture_module():
    return 20

@pytest.fixture(scope="session")#durante toda a execução do pytest. teardown após a execução.
def fixture_session():
    return 30

def test_1(fixture_function):
    assert fixture_function == 10

def test_2(fixture_function):
    assert fixture_function == 10 #aqui é uma nova instância, não compartilha de recurso.

def test_3(fixture_function, fixture_module):
    assert fixture_function == 10
    assert fixture_module == 20

def test_4(fixture_module, fixture_session):
    assert fixture_module == 20
    assert fixture_session == 30

def test_all_fixture(fixture_function, fixture_module, fixture_session):
    assert fixture_function == 10
    assert fixture_module == 20
    assert fixture_session == 30