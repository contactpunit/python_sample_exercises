from ds.ds.fibonacci_num import fib
import pytest


def test_raises_ValueError():
    with pytest.raises(ValueError):
        assert fib(-1)


def test_raises_TypeError():
    with pytest.raises(TypeError):
        assert fib('hello')


@pytest.mark.parametrize('num, expected', [
    (9, 34),
    (1, 1),
    (2, 1)
])
def test_fibonacci(num, expected):
    assert fib(num) == expected
