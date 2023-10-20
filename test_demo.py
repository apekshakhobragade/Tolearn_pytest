import pytest

@pytest.fixture
def setUp():
    print("launch the browser")
    print("start logging the websites")

def test_login(setUp):
    print("login successful")

def test_add1():
    print("calculation successful")
@pytest.mark.regression
def test_add():
    assert 2+3==5

@pytest.mark.skip
def test_login():
    print("login successful")

@pytest.mark.xfail
def test_login():
    print("login successful")