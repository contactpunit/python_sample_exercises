from ds.ds.nested_lc import get_all_jeeps, get_all_matching_models, get_first_model_each_manufacturer, \
    cars, sort_car_models
import pytest


def test_get_all_jeeps():
    assert get_all_jeeps(cars) == "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"


def test_get_all_jeeps_type_str():
    assert type(get_all_jeeps()) == str


def test_get_first_model_each_manufacturer():
    assert get_first_model_each_manufacturer(cars) == ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']


@pytest.mark.parametrize('grep', [
    'trail',
    'Trail',
    'TRAIL',
])
def test_get_all_matching_models(grep):
    assert get_all_matching_models(cars, grep=grep) == ['Trailblazer', 'Trailhawk']


@pytest.mark.parametrize('grep', [
    'Co',
    'CO',
])
def test_get_all_matching_models(grep):
    assert get_all_matching_models(cars, grep=grep) == ['Accord', 'Commodore', 'Falcon']


@pytest.mark.parametrize('car, models', [
    ('Ford', ['Fairlane', 'Falcon', 'Festiva', 'Focus']),
    ('Holden', ['Barina', 'Captiva', 'Commodore', 'Trailblazer']),
    ('Nissan', ['350Z', 'Maxima', 'Navara', 'Pulsar']),
    ('Honda', ['Accord', 'Civic', 'Jazz', 'Odyssey']),
    ('Jeep', ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'])
])
def test_sort_car_models_ford(car, models):
    assert sort_car_models(cars)[car] == models
