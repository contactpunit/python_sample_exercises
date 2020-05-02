import pytest
from ds.ds.palindrome import is_palindrome, get_longest_palindrome


@pytest.mark.parametrize('word', [
    'malayalam',
    'malay alam',
    'dont kik tnod'
])
def test_is_palindrome(word):
    assert is_palindrome(word)


@pytest.mark.parametrize('word', [
    'dont know man',
    'tets 123'
    'test'
])
def test_is_not_palindrome(word):
    assert not is_palindrome(word)
