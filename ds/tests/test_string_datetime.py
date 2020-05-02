import pytest
from datetime import datetime
from ds.ds.string_datetime import get_month_most_posts, convert_to_datetime, _get_dates


@pytest.fixture()
def generate_data():
    str_dates = _get_dates()
    return [convert_to_datetime(d) for d in str_dates]


@pytest.mark.parametrize('date_str, dateobj', [
    ('Thu, 04 May 2017 20:46:00 +0200', datetime(2017, 5, 4, 20, 46)),
    ('Wed, 22 Mar 2017 12:42:00 +0100', datetime(2017, 3, 22, 12, 42)),
    ('Mon, 20 Feb 2017 00:01:00 +0100', datetime(2017, 2, 20, 0, 1)),
    ('Sun, 07 Jan 2018 12:00:00 +0100', datetime(2018, 1, 7, 12, 0)),
    ('Sat, 15 Apr 2017 01:00:00 +0200', datetime(2017, 4, 15, 1, 0))
])
def test_convert_to_datetime(date_str, dateobj):
    assert convert_to_datetime(date_str) == dateobj


def test_get_month_most_posts(generate_data):
    assert get_month_most_posts(generate_data) == '2017-01'
