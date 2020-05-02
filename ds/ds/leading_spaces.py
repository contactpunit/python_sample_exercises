from itertools import takewhile


def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    required = takewhile(lambda x: x == ' ', text)
    return len(list(required))


