import pytest
from ds.ds.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("input_value, expected",
                         [(5, "Buzz"),
                          (1, 1),
                          (3, "Fizz"),
                          (15, "Fizz Buzz")])
def test_fizzbuzz_num(input_value, expected):
    assert fizzbuzz(input_value) == expected
