def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        lines = 0
        words = 0
        chars = 0
        for line in f:
            lines += 1
            for _ in line.strip().split():
                words += 1
            for _ in line:
                chars += 1
    return f'{lines} {words} {chars} {file_}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
