import pytest
import re
from ds.ds.extract_dict import get_users

pw4 = """
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
avar:x:1000:1000::/home/avar:/bin/bash
chad:x:1001:1001::/home/chad:/bin/bash
git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
"""


@pytest.fixture()
def process_passwd_file():
    return get_users(pw4)


@pytest.mark.parametrize('key, value', [
    ('git-svn-mirror', 'Git mirror'),
    ('artagnon', 'Ramkumar R Git GSOC')

])
def test_uid_to_name_mapping(process_passwd_file, key, value):
    r = process_passwd_file
    print(r)
    assert r['git-svn-mirror'] == 'Git mirror'
    assert r['artagnon'] == 'Ramkumar R Git GSOC'
