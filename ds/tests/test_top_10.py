import pytest
from collections import Counter
from ds.ds.top_10 import get_pybites_top_tags, tempfile


@pytest.fixture()
def parse_xml():
    with open(tempfile) as f:
        content = f.read().lower()
    return content


def test_check_top_n(parse_xml):
    content = parse_xml
    assert get_pybites_top_tags(5) == [('python', 79),
                                       ('learning', 79),
                                       ('codechallenges', 72),
                                       ('twitter', 62),
                                       ('tips', 61)]


def test_check_top_default(parse_xml):
    content = parse_xml
    assert get_pybites_top_tags() == [('python', 79),
                                      ('learning', 79),
                                      ('codechallenges', 72),
                                      ('twitter', 62),
                                      ('tips', 61),
                                      ('flask', 52),
                                      ('news', 49),
                                      ('django', 37),
                                      ('code', 25),
                                      ('github', 24)]
