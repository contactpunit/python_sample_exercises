import pytest
from ds.ds.round_down import round_up_or_down

trans1 = [2.05, 3.55, 4.50, 10.76, 100.25]
expected1 = [3, 4, 5, 11, 101]
expected2 = [2, 3, 4, 10, 100]


@pytest.mark.parametrize('data, up, expected', [
    (trans1, True, expected1),
    (trans1, False, expected2)
])
def test_round_up_down(data, up, expected):
    assert round_up_or_down(data, up) == expected
