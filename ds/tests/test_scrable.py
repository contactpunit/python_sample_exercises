import pytest
from ds.ds.scrable import load_words, calc_word_value, max_word_value


def test_check_num_words():
    assert len(load_words()) == 235886


@pytest.mark.parametrize('word, expected', [
    ('Zygobranchiata', 34),
    ('benzalphenylhydrazone', 56),
    ('JuliaN', 13)
])
def test_check_word_value(word, expected):
    assert calc_word_value(word) == expected


@pytest.mark.parametrize('words, maxword', [
    (['bob', 'julian', 'pybites', 'quit', 'barbeque'], 'barbeque')
])
def test_max_value(words, maxword):
    assert max_word_value(words) == maxword
