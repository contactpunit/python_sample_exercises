import pytest
from ds.ds.die_hard import gen_files, diehard_pybites, Stats


def test_gen_files():
    g = gen_files()
    assert next(g) == 'mridubhatnagar'
    assert next(g) == 'aleksandarknezevic'
    assert next(g) == 'Blair_Young'


def test_max_diehard_bytes():
    assert diehard_pybites() == Stats(user='clamytoe', challenge=('01', 7))


def test_returntype_diehard_bytes():
    assert diehard_pybites().__class__.__name__ == 'Stats'
