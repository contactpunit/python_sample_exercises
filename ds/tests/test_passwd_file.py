import pytest
from ds.ds.passwd_file import get_users_for_shell, PASSWD_OUTPUT, OTHER_PASSWD_OUTPUT


@pytest.fixture()
def create_passwd_file1(tmpdir_factory):
    file = tmpdir_factory.mktemp('data').join('test.txt')
    print(f'file created {file}')
    with open(file, 'w') as f:
        f.write(PASSWD_OUTPUT)
    return file


@pytest.fixture()
def create_passwd_file2(tmpdir_factory):
    file = tmpdir_factory.mktemp('data').join('test.txt')
    print(f'file created {file}')
    with open(file, 'w') as f:
        f.write(OTHER_PASSWD_OUTPUT)
    return file


expected1 = ['artagnon', 'avar', 'chad', 'gerrit2',
             'git-svn-mirror', 'root', 'ssh-rsa']

expected2 = ['invscout', 'jdoe', 'paul', 'root']


@pytest.mark.parametrize('expected', [
    expected1
])
def test_get_users1(create_passwd_file1, expected):
    file1 = create_passwd_file1
    f = open(file1)
    data1 = f.read()
    f.close()
    assert sorted(get_users_for_shell(data1)) == expected


@pytest.mark.parametrize('expected', [
    expected2
])
def test_get_user2(create_passwd_file2, expected):
    file2 = create_passwd_file2
    f = open(file2)
    data2 = f.read()
    f.close()
    print(data2)
    assert sorted(get_users_for_shell(data2, grep_shell='ksh')) == expected
