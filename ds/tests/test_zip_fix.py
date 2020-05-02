from ds.ds.zip_fix import get_attendees
import pytest


@pytest.mark.parametrize("expected", [
    ('Bob', 'ES', True),
    ('Mike', 'US', '-'),
    ('Kim', '-', '-'),
    ('Andre', '-', '-')
])
def test_zip_results(expected, capsys ):
    result = get_attendees()
    out, err = capsys.readouterr()
    assert str(expected) in out
