import pytest
from ds.ds.most_common_word import get_harry_most_common_word


def test_get_most_common():
    assert get_harry_most_common_word()[0] == 'dursley'


def test_return_type():
    assert get_harry_most_common_word().__class__ == tuple
