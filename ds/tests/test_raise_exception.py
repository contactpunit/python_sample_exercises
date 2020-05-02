import pytest
from ds.ds.raise_exceptions import positive_divide


@pytest.mark.parametrize('numerator, denominator', [
    (5, -1),
    (4, -2)
])
def test_raises_value_error(numerator, denominator):
    with pytest.raises(ValueError) as e:
        positive_divide(numerator, denominator)


@pytest.mark.parametrize('numerator, denominator', [
    (5, 0),
    (2, 0),
    (9, 0)
])
def test_raise_zero_division_error(numerator, denominator):
    assert positive_divide(numerator, denominator) == 0


@pytest.mark.parametrize('numerator, denominator', [
    (5, 'hello'),
    (-9, 'ole')
])
def test_raise_type_error(numerator, denominator):
    with pytest.raises(TypeError):
        positive_divide(numerator, denominator)
