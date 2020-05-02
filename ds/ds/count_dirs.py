import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    countd, countf = 0, 0
    for (dirpath, dirnames, filenames) in os.walk(directory):
        countd += len(dirnames)
        countf += len(filenames)
    return (countd, countf)


print(count_dirs_and_files('/tmp/a'))
