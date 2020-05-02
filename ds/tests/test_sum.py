from ds.ds.sum_num import sum_numbers
import pytest


def test_sum_with_inputs():
    assert (sum_numbers([1, 2, 3]) == 6)


def test_sum_without_inputs():
    assert sum_numbers() == 5050
