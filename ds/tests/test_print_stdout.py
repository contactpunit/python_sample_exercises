import pytest
from ds.ds.print_stdout import print_workout_days


@pytest.mark.parametrize('work, expected', [
    ('upper body #1', 'Mon'),
    ('lower body #1', 'Tue'),
    ('30 min cardio', 'Wed'),
    ('upper body #2', 'Thu'),
    ('lower body #2', 'Fri'),
    ('invalid', 'No matching workout'),
    ('upper body', 'Mon, Thu'),
    ('lower body', 'Tue, Fri')
])
def test_print_workout_days(capsys, work, expected):
    print_workout_days(work)
    out, err = capsys.readouterr()
    assert out.strip() == expected
