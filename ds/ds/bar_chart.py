import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

if not os.path.exists(SAFARI_LOGS):
    urllib.request.urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        SAFARI_LOGS
    )


def create_chart():
    d = defaultdict(list)
    with open(SAFARI_LOGS) as f:
        lines = f.readlines()
        lines_iter = iter(lines)
        previous = next(lines_iter)
    for line in lines:
        if 'sending to slack channel' in line:
            date, remain = previous.split(' ', 1)
            if 'python' in remain.lower():
                d[date.strip()].append(PY_BOOK)
            else:
                d[date.strip()].append(OTHER_BOOK)
        previous = line
    for k, v in d.items():
        print(f'{k} {"".join(v)}')


