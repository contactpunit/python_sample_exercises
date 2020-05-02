import pytest
from ds.ds.password_validate import validate_password, used_passwords


@pytest.mark.parametrize('word', [
    'hello',
    'HEELLOO'
])
def test_all_lower_all_upper(word):
    assert not validate_password(word)


@pytest.mark.parametrize('word', [
    '12345'
])
def test_all_numeric(word):
    assert not validate_password(word)


def test_valid_password():
    size = len(used_passwords)
    assert validate_password('We<3Python')
    assert len(used_passwords) == size + 1
