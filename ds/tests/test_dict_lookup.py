import pytest
from ds.ds.dict_lookup import get_person_age


@pytest.mark.parametrize('key, value', [
    ('ana', 26),
    ('thomas', 46)
])
def test_lookup_result(key, value):
    assert get_person_age(key) == value