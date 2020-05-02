import pytest
from ds.ds.user_validate import get_secret_token, UserDoesNotExist, UserNoPermission, UserAccessExpired


@pytest.mark.parametrize('user', [
    'Tim',
    'Bib'
])
def test_user_doesnot_exist(user):
    with pytest.raises(UserDoesNotExist):
        get_secret_token(user)


@pytest.mark.parametrize('user', [
    'Julian'
])
def test_user_no_permission(user):
    with pytest.raises(UserNoPermission):
        get_secret_token(user)


@pytest.mark.parametrize('user', [
    'Bob'
])
def test_user_expired(user):
    with pytest.raises(UserAccessExpired):
        get_secret_token(user)


@pytest.mark.parametrize('classname, exceptionclass', [
    (UserNoPermission, Exception),
    (UserAccessExpired, Exception),
    (UserDoesNotExist, Exception)
])
def test_new_classes_subclass_of_exception(classname, exceptionclass):
    assert issubclass(classname, exceptionclass)
