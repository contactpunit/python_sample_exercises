VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(True if char.lower() in VOWELS else False for char in input_str)


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(True if char.lower() in PYTHON else False for char in input_str)


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for char in input_str:
        if char.isnumeric():
            return True
    return False
