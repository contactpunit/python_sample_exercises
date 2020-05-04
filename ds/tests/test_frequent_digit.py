import pytest
from ds.ds.frequent_digit import freq_digit


@pytest.mark.parametrize('params, expected', [
    (123445, 4),
    (12345, 1),
    (2002, 2),
    (19944323222343443333, 3)
])
def test_check_frequent_digit(params, expected):
    pass
