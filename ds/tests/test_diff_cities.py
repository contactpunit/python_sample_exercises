import pytest
from ds.ds.diff_cities import uncommon_cities


@pytest.mark.parametrize('my_cities, other_cities, expected', [
    (['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin'],
     ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima'], 8),
    (['Rome', 'Paris', 'Madrid'], ['Chicago', 'Seville', 'Berlin'], 6)
])
def test_len_diff_cities(my_cities, other_cities, expected):
    assert uncommon_cities(my_cities, other_cities) == expected
