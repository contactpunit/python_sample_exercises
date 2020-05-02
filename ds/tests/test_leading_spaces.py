from ds.ds.leading_spaces import count_indents
import pytest

strings = ['   prodata',
           '  abcd',
           'string',
           '          who is the lord ?  ']

results = [3, 2, 0, 10]


@pytest.mark.parametrize('in_arg, expected',
                         [(string, count) for string, count in zip(strings, results)]
                         )
def test_num_spaces(in_arg, expected):
    assert count_indents(in_arg) == expected
