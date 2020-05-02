from enum import Enum
from ds.ds.list_equality import check_equality, Equality
import pytest

a = [1, 2, 3, 4]
b = a


@pytest.mark.parametrize('list1, list2, result', [
    (a, a[:], Equality.SAME_ORDERED),
    (a, a[::-1], Equality.SAME_UNORDERED),
    (a, b, Equality.SAME_REFERENCE)
])
def test_equality_inequality_cases(list1, list2, result):
    assert check_equality(list1, list2) == result
