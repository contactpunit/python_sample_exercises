import pytest
from ds.ds.transpose_ds import transpose
from collections import namedtuple

Member = namedtuple('Member', 'name, since_days, karma_points, bitecoin_earned')
data1 = [Member(name='Bob', since_days=60, karma_points=60,
                bitecoin_earned=56),
         Member(name='Julian', since_days=221, karma_points=34,
                bitecoin_earned=78)]

data2 = {'2017-8': 19, '2017-9': 13}


@pytest.mark.parametrize('data1, expected', [
    (data1, [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)])
])
def test_transpose_namedtuple(data1, expected):
    assert transpose(data1) == expected


@pytest.mark.parametrize('data2, expected', [
    (data2, [('2017-8', '2017-9'), (19, 13)])
])
def test_transpose_dict(data2, expected):
    assert transpose(data2) == expected
