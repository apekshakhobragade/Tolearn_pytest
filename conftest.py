import pytest


@pytest.fixture(autouse=True)
def setUp():
    print("launch the browser")
    print("login the websites")
    yield
    print("close the browser")