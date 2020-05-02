from ds.ds.prop import Promo
from datetime import datetime, timedelta
import pytest


@pytest.mark.parametrize('name, check_time', [
    ('punit', timedelta(days=-1)),
    ('nidhi', timedelta(days=-2)),
    ('vkjain', timedelta(days=-11))
])
def test_expired(name, check_time):
    assert helper(name, check_time)


@pytest.mark.parametrize('name, check_time', [
    ('punit', timedelta(days=1)),
    ('nidhi', timedelta(days=2)),
    ('vkjain', timedelta(seconds=1))
])
def test_not_expired(name, check_time):
    assert not helper(name, check_time)


def helper(name, t):
    present = datetime.now() + t
    p = Promo(name, present)
    return p.expired
