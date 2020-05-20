import pytest
from ds.ds.common_language import common_languages

d = {'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
     'paul': ['C++', 'JS', 'Python'],
     'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
     'tim': ['Python', 'Haskell', 'C++', 'JS']}


@pytest.mark.parametrize('input_dict, result', [
    (d, {'JS', 'Python'})
])
def test_common_languages(input_dict, result):
    assert common_languages(input_dict) == result
