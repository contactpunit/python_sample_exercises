from ds.ds.tail_display import tail
import pytest

content = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


@pytest.mark.parametrize('content, num_lines, expected', [
    (content, 2, content.split('\n')[-2:]),
    (content, 4, content.split('\n')[-4:]),
])
def test_last_2_lines(content, num_lines, expected, tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "a.txt"
    p.write_text(content)
    assert tail(p, num_lines) == expected
