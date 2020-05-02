import pytest
from ds.ds.running_avg import running_mean


@pytest.mark.parametrize('orig, expected', [
    ([10, 20, 30], [10.0, 15.0, 20.0]),
    ([], []),
    ([3, 4, 6, 2, 1, 9, 0, 7, 5, 8],
     [3.0, 3.5, 4.33, 3.75, 3.2, 4.17, 3.57, 4.0, 4.11, 4.5]),
    ([2, 6, 10, 8, 11, 10],
     [2.0, 4.0, 6.0, 6.5, 7.4, 7.83]),
])
def test_check_running_average(orig, expected):
    assert list(running_mean(orig)) == expected
