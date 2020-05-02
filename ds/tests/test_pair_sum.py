import pytest
from ds.ds.pair_sum import find_number_pairs


@pytest.mark.parametrize('pair, total, expected', [
    ([2, 3, 5, 4, 6], 10, [(4, 6)]),
    ([9, 1, 3, 8, 7], 10, [(9, 1), (3, 7)])
])
def test_all_pairs(pair, total, expected):
    assert find_number_pairs(pair, total) == expected
