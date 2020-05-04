import pytest

from ds.ds.numbers_to_dec import list_to_decimal


@pytest.mark.parametrize('keys', [
    [1, 11, 13],
    [2, 6, 9, 10],
    [-3, 1, 3]

])
def test_raise_ValueError(keys):
    with pytest.raises(ValueError):
        list_to_decimal(keys)


@pytest.mark.parametrize('keys', [
    [6, 2, True],
    [3.6, 4, 1],
    ['4', 5, 3, 1]
])
def test_bool_raise_TypeError(keys):
    with pytest.raises(TypeError):
        list_to_decimal(keys)


@pytest.mark.parametrize('keys, expected', [
    ([0, 4, 2, 8], 428),
    ([1, 2], 12),
    ([3], 3)
])
def test_decimal_place(keys, expected):
    assert list_to_decimal(keys) == expected
