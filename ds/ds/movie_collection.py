import csv
import os
import statistics
from collections import namedtuple, defaultdict, Counter

Directors = namedtuple('Directors', 'director_name imdb_score movie_title title_year')


def read_csv_data(filename):
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        movies = []
        for line in reader:
            movies.append(line)
        # print(movies[:1])
    return movies


def movies_after_1960(movies):
    movies = [movie
              for movie in movies
              if movie['title_year'] and int(movie['title_year']) >= 1960
              ]
    return movies


def movies_with_min_dir(movies):
    movies_with_dir = defaultdict(list)
    for movie in movies:
        m = Directors(director_name=movie['director_name'],
                      imdb_score=movie['imdb_score'], movie_title=movie['movie_title'], title_year=movie['title_year'])
        movies_with_dir[movie['director_name']].append(m)
    return movies_with_dir
    # for k,v in movies_with_dir.items():
    #     print('{} --- {}'.format(k, len(v)))


def top_rated_dirs(movies_with_dirs):
    movies_with_dirs = {m: v for m, v in movies_with_dirs.items() if len(v) >= 4}
    top_dir = sorted(movies_with_dirs.items(), key=lambda k: _helper(k[1]), reverse=True)
    for index, entry in enumerate(top_dir, 1):
        print(f'{index}.  {entry[0]} {_helper(entry[1]):>20}')
        print('_____________________________________________')
        for e in sorted(entry[1], key=lambda k: k.imdb_score, reverse=True):
            print(f'{e.title_year}]  {e.movie_title} {e.imdb_score:>20}')
            if index > 4:
                return


def _helper(v):
    count = 0
    score = 0
    for entry in v:
        count += 1
        score += float(entry.imdb_score)
    return score / count


def main():
    filename = os.path.join('../..', 'data', 'movie_metadata.csv')
    if filename:
        movies = read_csv_data(filename)
        movies = movies_after_1960(movies)
        movies_with_dirs = movies_with_min_dir(movies)
        top_rated_dirs(movies_with_dirs)


if __name__ == '__main__':
    main()
