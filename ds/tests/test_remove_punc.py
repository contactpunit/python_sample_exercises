import pytest
from ds.ds.remove_punc import remove_punctuation


@pytest.mark.parametrize('original, expected', [
    ('Hello, I am Tim.', 'Hello I am Tim'),
    (';String. with. punctuation characters!',
     'String with punctuation characters'),
    ('Watch out!!!', 'Watch out'),
    ('Spaces - should - work the same, yes?',
     'Spaces  should  work the same yes'),
    ("Some other (chars) |:-^, let's delete them",
     'Some other chars  lets delete them')
])
def test_remove_chars(original, expected):
    assert remove_punctuation(original) == expected
