import pytest
from ds.ds.table_sequence import generate_table, names, aliases, points
import random


def random_nums():
    random.seed(0)
    return random.sample(range(81, 101), 6)


points = random_nums()
check1 = [names, aliases]
check2 = [names, aliases, points]


@pytest.mark.parametrize('seq, result', [
    (check1,
     ['Julian | Pythonista', 'Bob | Nerd', 'PyBites | Coder', 'Dante | Pythonista', 'Martin | Nerd',
      'Rodolfo | Coder']),
    (check2,
     ['Julian | Pythonista | 93', 'Bob | Nerd | 94', 'PyBites | Coder | 82', 'Dante | Pythonista | 89',
      'Martin | Nerd | 96', 'Rodolfo | Coder | 87'])
])
def test_table_values(seq, result):
    assert generate_table(*seq) == result
