import pytest
import json
from ds.ds.dict_to_namedtuple import dict2nt, nt2json, blog


@pytest.fixture()
def get_np():
    return dict2nt(blog)


@pytest.mark.parametrize('d', [
    blog
])
def test_dict_2_nt_classname(d):
    assert dict2nt(d).__class__.__name__ == 'Blog'


def test_dict_2_nt(get_np):
    result = get_np
    assert result.name == 'PyBites'
    assert result.tags == ['Python', 'Code Challenges', 'Learn by Doing']
    assert type(result.started).__name__ == 'datetime'
    assert result.site == 'https://pybit.es'
    assert result.__class__.__base__ == tuple


def test_nt2json(get_np):
    np = get_np
    js = nt2json(np)
    assert js.__class__.__name__ == 'str'
    j = json.loads(js)
    assert j['name'] == 'PyBites'
    assert j['tags'] == ['Python', 'Code Challenges', 'Learn by Doing']
