import pytest

@pytest.fixture
def take_value():
    i = 20
    return i

def test_new_fun(take_value):
    assert take_value + 10 == 30

def test_new2_fun(take_value):
    assert take_value - 10 == 10  # Adjusted assertion to be correct
