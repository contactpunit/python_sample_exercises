import pytest
from ds.ds.match_strings import contains_any_py_chars, contains_digits, contains_only_vowels


@pytest.mark.parametrize('input_str, result', [
    ('aioue', True),
    ('EoUia', True),
    ('aaAiIee', True),
    ('AEIOU', True),
    ('aaeeouu', True),
    ('abcde', False),
    ('AE123', False),
    ('AiOuef', False)
])
def test_check_only_vowels(input_str, result):
    assert contains_only_vowels(input_str) == result


@pytest.mark.parametrize('input_str, result', [
    ('yes1', True),
    ('123', True),
    ('hello2', True),
    ('up2date', True),
    ('yes', False),
    ('hello', False),
    ('', False)
])
def test_check_digits(input_str, result):
    assert contains_digits(input_str) == result


@pytest.mark.parametrize('input_str, result', [
    ('Python', True),
    ('pycharm', True),
    ('PYTHON', True),
    ('teaser', True),
    ('bob', True),
    ('julian', True),
    ('yes', True),
    ('no', True),
    ('america', False),
    ('B@b', False),
    ('Jules', False),
    ('agua', False),
    ('123', False),
    ('', False)
])
def test_check_contain_py_char(input_str, result):
    assert bool(contains_any_py_chars(input_str)) is result
