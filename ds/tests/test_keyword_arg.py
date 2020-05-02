from ds.ds.keyword_arg import get_profile
import pytest


def test_check_keyword_arg():
    assert get_profile() == 'julian is a programmer'


@pytest.mark.parametrize('key', [
    'Punit',
    'Nidhi'
])
def test_raise_error_when_not_keyword_arg(key):
    with pytest.raises(TypeError):
        get_profile(key, profession='engineer')


def test_typeerror_when_wrong_key_passed():
    with pytest.raises(TypeError):
        get_profile(hello='punit')


def test_wrong_additional_flag():
    with pytest.raises(TypeError):
        get_profile(name='rambo', profession='killer', country='US')
