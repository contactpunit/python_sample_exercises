import pytest
from ds.ds.sort_words import sort_words_case_insensitively

inp1 = ("It's almost Holidays and PyBites wishes You a "
        "Merry Christmas and a Happy 2019").split()
out1 = ['a', 'a', 'almost', 'and', 'and', 'Christmas',
        'Happy', 'Holidays', "It's", 'Merry', 'PyBites',
        'wishes', 'You', '2019']


@pytest.mark.parametrize('input_string, expected', [
    (inp1, out1)
])
def test_sorted_words(input_string, expected):
    assert sort_words_case_insensitively(input_string) == expected
