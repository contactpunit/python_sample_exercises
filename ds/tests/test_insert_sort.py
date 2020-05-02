import pytest
from ds.ds.insert_sort import OrderedList


@pytest.fixture(scope='module')
def get_initial_list():
    l = OrderedList()
    l.add(1)
    l.add(5)
    return l


@pytest.mark.parametrize('key, expected', [
    (2, '1, 2, 5'),
    (6, '1, 2, 5, 6')
])
def test_insert_is_sorted(get_initial_list, key, expected):
    l = get_initial_list
    l.add(key)
    assert str(l) == expected
