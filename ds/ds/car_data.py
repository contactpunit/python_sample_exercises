from collections import Counter, defaultdict
import requests


def automaker():
    return defaultdict(set)


CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    result = defaultdict(automaker)
    for entry in data:
        result[entry['year']][entry['automaker']].add(entry['model'])
    return sorted(result[year].items(), key=lambda k: len(k[1]), reverse=True)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    result = defaultdict(set)
    for entry in data:
        result[(entry['automaker'], entry['year'])].add(entry['model'])
    return result[(automaker, year)]
