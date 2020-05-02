import pytest
import re
from ds.ds.total_duration import calc_total_course_duration, get_all_timestamps


@pytest.fixture(scope='module')
def generate_timestring():
    return get_all_timestamps()


@pytest.mark.parametrize('index', [
    1, 2, 3
])
def test_get_all_timestamps(generate_timestring, index):
    t = generate_timestring
    assert re.search(r'\d+:\d+', t[index])


def test_calc_total_course_duration(generate_timestring):
    t = generate_timestring
    assert calc_total_course_duration(t) == '6:50:31'
