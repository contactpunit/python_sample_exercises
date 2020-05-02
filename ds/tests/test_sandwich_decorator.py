import pytest
from ds.ds.sandwich_decorator import sandwich, UPPER_SLICE


@pytest.fixture()
@sandwich
def string_of_all_elements():
    print(', '.join(['crab', 'furnace', 'coal', 'roast']))


def test_printed_value(capsys, string_of_all_elements):
    string_of_all_elements
    out, err = capsys.readouterr()
    assert UPPER_SLICE in out
