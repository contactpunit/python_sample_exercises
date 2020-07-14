from collections import Counter, defaultdict
import csv
import re

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
      which is a mapping of episode=>words spoken"""
    d = defaultdict(Counter)
    csvreader = csv.reader(content.splitlines())
    for row in csvreader:
        # print(row)
        episode = row[1]
        character = row[2]
        words = row[3]
        d[character][episode] += char_count(words)
    return d


def char_count(words):
    return len([word for word in words.split(' ') if word not in '?.\"'])
