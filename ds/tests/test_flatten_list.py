import pytest
from ds.ds.flatten_list import flatten

r = ['a', 'b', [1, 2, 3],
     ['c', 'd', ['e', 'f', ['g', 'h']]],
     [4, [5, 6, [7, [8]]]]]


def test_check_flattened_list_returned():
    assert list(flatten(r)) == ['a', 'b', 1, 2, 3, 'c', 'd', 'e', 'f', 'g', 'h', 4, 5, 6, 7, 8]
