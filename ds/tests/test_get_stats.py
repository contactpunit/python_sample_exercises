import pytest
from ds.ds.get_stats import get_all_line_counts, create_stats_report, STATS


@pytest.fixture()
def get_stats_data():
    result = get_all_line_counts(STATS)
    return result


expected = '''- count     :     186
- min       :       6
- max       :     337
- mean      :   43.74'''


@pytest.fixture()
def get_stats_report():
    report = create_stats_report(get_all_line_counts(STATS))
    return report


@pytest.mark.parametrize('expected_val', [
    expected.split('\n')[0],
    expected.split('\n')[1],
    expected.split('\n')[2],
    expected.split('\n')[3]
])
def test_stats_match(get_stats_report, expected_val):
    report = get_stats_report
    assert expected_val in report


def test_record_length_match(get_stats_data):
    assert len(get_stats_data) == 186
