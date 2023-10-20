import pytest


def test_showoff():
    print("msg wil be successfully displayed")

def test_adddisplay():
    print("to display the code")

@pytest.mark.sanity
def test_screen():
    assert 4+8==10

