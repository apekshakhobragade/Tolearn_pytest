import pytest

# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)

@pytest.mark.parametrize("a, b, final", [(2,7, 9), (3, 8 ,11)])
def testadd(a,b,final):
    assert a+b == final
