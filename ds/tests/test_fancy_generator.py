import pytest
from ds.ds.fancy_generator import countdown


@pytest.fixture()
def get_generator_obj():
    c = countdown()
    return c


def test_generator_values(get_generator_obj):
    g = get_generator_obj
    assert next(g) == 100
    j = 99
    for i in g:
        assert i == j
        j -= 1