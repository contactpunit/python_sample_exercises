import pytest
from pathlib import Path
from urllib.request import urlretrieve
from ds.ds.omdb_movie import get_movie_longest_runtime, get_movie_data, get_movie_most_nominations, get_single_comedy

TMP = Path('/tmp')
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)


@pytest.fixture(scope='module')
def read_file_data():
    data = get_movie_data([DATA_LOCAL])
    return data


def test_get_movie_data(read_file_data):
    jsondata = read_file_data
    assert len(jsondata) == 5
    assert jsondata[0]['Title'] == 'The Terminator'


def test_get_movie_longest_runtime(read_file_data):
    assert get_movie_longest_runtime(read_file_data) == 'Blade Runner 2049'


def test_get_movie_most_nominations(read_file_data):
    assert get_movie_most_nominations(read_file_data) == 'Fight Club'


def test_get_single_comedy(read_file_data):
    assert get_single_comedy(read_file_data) == 'Horrible Bosses'
