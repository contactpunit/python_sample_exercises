import pytest
from ds.ds.custom_wc import wc

lines = ['Hello world',
         'Keep calm and code in Python',
         'Have a nice weekend']


@pytest.mark.parametrize('content, expected', [
    ('Hello world', '1 2 11'),
    ('\n'.join(lines[:2]), '2 8 40')
])
def test_count_lines_words_chars(content, expected, tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "a.txt"
    p.write_text(content)
    assert wc(p) == f'{expected} {p}'
