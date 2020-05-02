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
    for k, v in read_data().items():
        print(f'{k} {"".join(v)}')

def read_data():
    d = defaultdict(list)
    with open(SAFARI_LOGS) as f:
        data = f.readlines()
        iter_data = iter(data)
        parse_gen = _process_data(iter_data)
        next(parse_gen)
        while True:
            p_data = parse_gen.send('sending')
            if not p_data:
                break
            date, remain = p_data.split(' ', 1)
            if 'python' in remain.lower():
                d[date.strip()].append(PY_BOOK)
            else:
                d[date.strip()].append(OTHER_BOOK)
        return d


def _process_data(data):
    for line in data:
        if 'sending to slack channel' in line:
            books_line = next(data)
            check = yield books_line
            # print('moving ahead')
    yield None


create_chart()
