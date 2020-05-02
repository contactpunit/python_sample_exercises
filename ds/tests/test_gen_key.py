from ds.ds.gen_key import gen_key
import pytest


def test_default_length_is_correct():
    assert len(gen_key()) == 35


def test_modified_length_is_correct():
    assert len(gen_key(parts=2, chars_per_part=5)) == 11


def test_all_alphanumeric():
    result = gen_key()
    for part in result.split('-'):
        assert part.isalnum()


def test_number_of_parts():
    result = gen_key(parts=5, chars_per_part=4)
    parts = result.split('-')
    assert len(parts) == 5
