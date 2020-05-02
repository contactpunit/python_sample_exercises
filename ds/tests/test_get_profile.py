import pytest
from ds.ds.get_profile import get_profile


def test_get_profile_no_args():
    with pytest.raises(TypeError):
        get_profile()


def test_get_profile_non_int_age():
    with pytest.raises(ValueError):
        get_profile('punit', 'hello')


def test_get_profile_raises_Value_Error_args_morethan_5():
    with pytest.raises(ValueError):
        get_profile('punit', 43, 2, 5, 6, 7, 8, 9)


@pytest.mark.parametrize('name, age, args, expected', [
    ('punit', 42, [10, 12], {'name': 'punit', 'age': 42, 'sports': [10, 12]}),
])
def test_get_profile_return_correct_result_no_kwargs(name, age, args, expected):
    assert get_profile(name, age, *args) == expected


@pytest.mark.parametrize('name, age, args, kwargs, expected', [
    ('punit', 42, [10, 12], {'champ': 'helped out team in crisis'},
     {'name': 'punit', 'age': 42, 'sports': [10, 12], 'awards': {'champ': 'helped out team in crisis'}}),
])
def test_get_profile_return_correct_result_with_kwargs(name, age, args, kwargs, expected):
    assert get_profile(name, age, *args, **kwargs) == expected
