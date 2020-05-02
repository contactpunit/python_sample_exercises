from ds.ds.martiniq import get_index_different_char
import pytest

inputs = (
    ['A', 'f', '.', 'Q', 2],
    ['.', '{', ' ^', '%', 'a'],
    [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
    ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
    list(range(1, 9)) + ['}'] + list('abcde'),  # noqa E230
    [2, '.', ',', '!']
)
expected = [2, 4, 1, 5, 8, 0]


def create_params(inputs, expected):
    return [(inparam, outparam) for inparam, outparam in zip(inputs, expected)]


@pytest.mark.parametrize('input, expectedvalue',
                         create_params(inputs, expected)
                         )
def test_different_char(input, expectedvalue):
    assert get_index_different_char(input) == expectedvalue
