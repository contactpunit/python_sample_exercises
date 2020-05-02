from ds.ds.rotate import rotate
import pytest


@pytest.mark.parametrize("string, num, expected_value",
                         [('hello', 2, 'llohe'),
                          ('hello', -2, 'lohel')
                          ])
def test_rotate_with_different_params(string, num, expected_value):
    assert rotate(string, num) == expected_value
