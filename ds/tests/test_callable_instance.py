import pytest
from ds.ds.callable_instance import RecordScore


@pytest.fixture(scope='session')
def get_record_object():
    record = RecordScore()
    return record


@pytest.mark.parametrize('nextvalue, result', [
    (0, 0),
    (1, 1),
    (-1, 1),
    (9, 9),
    (7, 9)
])
def test_max_score(get_record_object, nextvalue, result):
    assert get_record_object(nextvalue) == result


def test_multiple_objects_score():
    record = RecordScore()
    assert record(10) == 10
    record(20)
    record(-10)
    record(35)
    record(-1)
    assert record(9) == 35
    record = RecordScore()
    record(-6)
    record(-1)
    record(-3)
    assert record(-5) == -1
