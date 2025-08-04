import pytest

@pytest.mark.a
def test_result():
    assert 5*5 == 25

@pytest.mark.b
def test_result2():
    assert 5*2 == 10