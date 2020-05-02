import pytest
from ds.ds.xml_elemtree import get_movies, get_tree, get_movie_longest_runtime, ET


@pytest.fixture()
def get_type_of_etree():
    t = get_tree()
    return t


def test_check_etree_type(get_type_of_etree):
    result = get_type_of_etree
    assert type(result) in [ET.ElementTree, ET.Element]


def test_match_movies():
    r = get_movies()
    assert list(r) == ['The Prestige', 'The Dark Knight', 'The Dark Knight Rises', 'Dunkirk', 'Interstellar']


def test_longest_movie():
    assert get_movie_longest_runtime() == 'Interstellar'
