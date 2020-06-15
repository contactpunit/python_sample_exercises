import pytest
from ..ds.dicts_and_lists import get_every_nth_state, get_longest_state, get_state_abbrev, \
    combine_state_names_and_abbreviations, states, us_state_abbrev


@pytest.mark.parametrize('place, result', [
    (10, ['Massachusetts', 'Missouri', 'Hawaii', 'Vermont', 'Delaware'])
])
def test_get_every_nth_state(place, result):
    assert get_every_nth_state(states, place) == result


def test_get_longest_state():
    assert get_longest_state(states) in ['South Carolina', 'North Carolina']


@pytest.mark.parametrize('state, result', [
    ('Nevada', 'NV'),
    ('New Mexico', 'NM'),
    ('South Carolina', 'SC'),
    ('junk', 'N/A')
])
def test_get_state_abbrev(state, result):
    assert get_state_abbrev(state) == result


def test_combine_state_names_and_abbreviations():
    assert combine_state_names_and_abbreviations() == ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
