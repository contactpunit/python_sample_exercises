import pytest
from ds.ds.local_globals import sum_numbers


@pytest.mark.parametrize('numbers, total, global_value', [
    ([], 0, -1),
    ([1, 2], 3, -1),
    ([99, 1, 10], 110, 0),
    ([140, 50, 10], 200, 2)
])
def test_global_value(numbers, total, global_value):
    assert sum_numbers(numbers) == total
    from ds.ds.local_globals import num_hundreds
    assert  num_hundreds == global_value
