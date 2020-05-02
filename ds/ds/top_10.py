import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as etree

# prep
tempfile = os.path.join('/tmp', 'feed')
if not os.path.exists(tempfile):
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/feed',
        tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    c = Counter()
    root = etree.fromstring(content)
    for child in root.iter('category'):
        c[child.text] += 1
    return c.most_common(n)
