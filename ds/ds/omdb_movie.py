import json
from collections import Counter


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            # jsonfile = json.load(f)
            # movies.append(jsonfile)
            for line in f:
                movies.append(json.loads(line.strip()))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return ','.join(
        [
            movie['Title']
            for movie in movies
            if 'Comedy' in movie['Genre']
        ]
    )


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    c = Counter()
    for movie in movies:
        c[movie['Title']] = int(movie['imdbVotes'].replace(',', ''))
    return c.most_common(1)[0][0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    c = Counter()
    for movie in movies:
        c[movie['Title']] = int(movie['Runtime'].split()[0])
    return c.most_common(1)[0][0]


# print(get_movie_most_nominations(get_movie_data(['/tmp/omdb_data'])))


get_movie_data(['/tmp/omdb_data'])
