import pytest
from ds.ds.car_data import most_prolific_automaker, get_models


@pytest.mark.parametrize('year, expected', [
    (2008, 'Toyota'),
    (1999, 'Dodge'),
    (2013, 'Hyundai')
])
def test_most_prolific_automaker(year, expected):
    assert most_prolific_automaker(year) == expected


@pytest.mark.parametrize('automaker, year, expected', [
    ('Mercedes-Benz', 2007, 'SL-Class'),
    ('Mercedes-Benz', 2007, 'GL-Class'),
    ('Mercedes-Benz', 2007, 'CL-Class')
])
def test_get_models(automaker, year, expected):
    assert expected in get_models(automaker, year)
