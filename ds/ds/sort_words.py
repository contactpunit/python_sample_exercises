import itertools


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    sorted_words = sorted(words, key=lambda word: word.lower())
    nums = itertools.takewhile(lambda x: str(x)[0] in list(map(str, range(0, 10))), sorted_words)
    remain = itertools.dropwhile(lambda x: str(x)[0] in list(map(str, range(0, 10))), sorted_words)
    return list(remain) + list(nums)


words = ("It's almost Holidays and PyBites wishes You a "
         "Merry Christmas and a Happy 2019").split()

