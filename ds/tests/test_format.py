from ds.ds.format_exercise import print_hanging_indents, poem
import pytest

expected = """Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""


def test_print_formatted_poem(capsys):
    print_hanging_indents(poem)
    out, err = capsys.readouterr()
    assert out == expected
