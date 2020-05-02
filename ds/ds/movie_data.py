import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
if not os.path.exists(local):
    urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    d = defaultdict(list)
    with open(MOVIE_DATA) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if int(row['title_year']) >= MIN_YEAR:
                    m = Movie(row['movie_title'], int(row['title_year']), float(row['imdb_score']))
                    d[row['director_name']].append(m)
            except ValueError:
                pass
    return d


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total = sum(movie.score for movie in movies)
    return round(total / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    t = []
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            average_score = round(sum([movie.score for movie in movies]) / len(movies), 1)
            t.append((director, average_score))
    return sorted(t, key=lambda e: e[1], reverse=True)


print(get_average_scores(get_movies_by_director()))
# print(get_movies_by_director())
