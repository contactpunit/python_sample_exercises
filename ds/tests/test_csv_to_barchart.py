import pytest
from ds.ds.csv_to_barchart import create_user_bar_chart, get_csv


@pytest.fixture(scope='module')
def return_csv():
    return get_csv()


def test_csv_entry(return_csv):
    assert '191e6477-a57c-4830-ac4d-9585e9e4c040,Jelle,America/Denver' in return_csv


@pytest.mark.parametrize('entry', [
    'America/Denver       | ++++',
    'Asia/Kolkata         | +++++++++++++',
    'Asia/Istanbul        | ++',
    'America/Los_Angeles  | +++++++++++++++++++++++++++++++++++'
])
def test_create_user_bar_chart(return_csv, capsys, entry):
    create_user_bar_chart(return_csv)
    out, err = capsys.readouterr()
    assert entry in out
