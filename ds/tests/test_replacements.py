from ds.ds.count_replacements import strip_vowels, text
import pytest

data = '''This is a test
        file for check'''

replaced = '''Th*s *s * t*st
        f*l* f*r ch*ck'''


def test_replacement_zen_of_python():
    output, num_replacements = strip_vowels(text)
    assert num_replacements == 264


def test_num_replacement():
    output, num_replacements = strip_vowels(data)
    assert num_replacements == 8
    assert output == replaced
