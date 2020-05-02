import pytest
from ds.ds.login_required import welcome


@pytest.mark.parametrize('user', [
    'ram',
    'shyam'
])
def test_invalid_user(user):
    assert welcome(user) == 'please create an account'


@pytest.mark.parametrize('user', [
    'julian',
    'carmen'
])
def test_not_logged_in_user(user):
    assert welcome(user) == 'please login'


@pytest.mark.parametrize('user', [
    'mike',
    'sue'
])
def test_valid_loggedin_user(user):
    assert welcome(user) == f'welcome back {user}'
