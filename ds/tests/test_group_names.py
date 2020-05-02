import pytest
from ds.ds.group_names import group_names_by_country, data


@pytest.fixture()
def get_result():
    result = group_names_by_country(data)
    return result


@pytest.mark.parametrize('key, expected', [
    ('ID', ['Husain Watsham', 'Sula Wasielewski']),
    ('BR', ['Alphonso Harrold']),
    ('CN', ['Margo Apdell', 'Ines Parrett', 'Davie Halbard']),
    ('PL', ['Kermit Braunle'])
])
def test_check_each_key_value_pair(get_result, key, expected):
    assert get_result[key] == expected
