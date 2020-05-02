import pytest
from ds.ds.queue_data import my_queue

expected = """
(0, [0])
(1, [0, 1])
(2, [0, 1, 2])
(3, [0, 1, 2, 3])
(4, [0, 1, 2, 3, 4])
(5, [1, 2, 3, 4, 5])
(6, [2, 3, 4, 5, 6])
(7, [3, 4, 5, 6, 7])
(8, [4, 5, 6, 7, 8])
(9, [5, 6, 7, 8, 9])
"""


@pytest.fixture()
def create_and_add_to_queue():
    result = []
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        result.append(f'({i}, {list(mq)})')
    return result


def test_one_line_output(create_and_add_to_queue, capsys):
    result = create_and_add_to_queue
    print(result)
    out, err = capsys.readouterr()
    assert '(0, [0])' in out
    assert '(9, [5, 6, 7, 8, 9])' in out
    assert '(4, [0, 1, 2, 3, 4])' in out
