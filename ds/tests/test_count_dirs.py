import pytest
from ds.ds.count_dirs import count_dirs_and_files

CONTENT = "demo content"


@pytest.fixture()
def create_file_dir_structure(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    e = d / 'sub1'
    e.mkdir()
    f = d / 'sub2'
    f.mkdir()
    k = d / 'sub3'
    k.mkdir()
    p = e / 'hello1.txt'
    p.write_text(CONTENT)
    q = f / 'hello2.txt'
    q.write_text(CONTENT)
    return d


def test_count_files_dirs(create_file_dir_structure):
    assert count_dirs_and_files(create_file_dir_structure) == (3, 2)
