import pytest
from ds.ds.custom_iterator import EggCreator
import random


@pytest.fixture()
def random_fix():
    random.seed(0)


@pytest.mark.parametrize('count, result', [
    (5, 'yellow egg\nyellow egg\nred egg\ngreen egg\nbrown egg\n'),
    (4, 'yellow egg\nyellow egg\nred egg\ngreen egg\n')
])
def test_is_iterator(random_fix, capfd, count, result):
    for e in EggCreator(count):
        print(e)
    out, err = capfd.readouterr()
    assert out == result


@pytest.mark.parametrize('count, result', [
    (5, 5),
    (4, 4)
])
def test_length_of_results_from_iterator(capfd, count, result):
    for e in EggCreator(count):
        print(e)
    out, err = capfd.readouterr()
    lines = out.split('\n')
    assert len(lines) - 1 == result


def test_stop_iteration():
    e = EggCreator(5)
    next(e)
    next(e)
    next(e)
    next(e)
    next(e)
    with pytest.raises(StopIteration):
        next(e)
