import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add_normal(calc):
    assert calc.add(2, 3) == 5


def test_add_negative(calc):
    assert calc.add(-4, 2) == -2


def test_subtract_normal(calc):
    assert calc.subtract(10, 4) == 6


def test_subtract_negative(calc):
    assert calc.subtract(-5, -3) == -2


def test_multiply_normal(calc):
    assert calc.multiply(3, 4) == 12


def test_multiply_negative(calc):
    assert calc.multiply(-2, 5) == -10


def test_divide_normal(calc):
    assert calc.divide(10, 2) == 5


def test_divide_negative(calc):
    assert calc.divide(-8, 2) == -4


def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)
