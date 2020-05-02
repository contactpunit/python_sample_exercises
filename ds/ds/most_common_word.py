import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
special_chars = list('-\';?:!.",')
if not os.path.exists(stopwords_file):
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
        stopwords_file
    )
if not os.path.exists(harry_text):
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
        harry_text
    )

with open(stopwords_file) as f:
    stopwords = [line.strip().lower() for line in f]


def get_harry_most_common_word():
    c = Counter()
    with open(harry_text) as h:
        for line in h:
            for word in line.split():
                if word.strip() and word.strip().lower() not in stopwords:
                    w = ''.join([letter.lower() for letter in word.strip() if letter not in special_chars])
                    if w:
                        c[w] += 1
    return c.most_common(1)[0]

print(get_harry_most_common_word())
