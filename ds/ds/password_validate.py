import string
from collections import defaultdict

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if not len(password) >= 6 and not len(password) <= 12:
        return False
    if password in used_passwords:
        return False
    charmap = _prepare_map(password)
    if not len(charmap['digit']) >= 1:
        return False
    if not len(charmap['lower']) >= 2:
        return False
    if not len(charmap['upper']) >= 1:
        return False
    if not len(charmap['punc']) >= 1:
        return False
    used_passwords.add(password)
    return True


def _prepare_map(password):
    d = defaultdict(list)
    for char in password:
        if digit(char):
            d['digit'].append(char)
        elif alpha(char) and upper(char):
            d['upper'].append(char)
        elif alpha(char) and lower(char):
            d['lower'].append(char)
        elif punc(char):
            d['punc'].append(char)
    return d


digit = lambda w: w.isdigit()
alpha = lambda a: a.isalpha()
lower = lambda l: l.islower()
upper = lambda u: u.isupper()
punc = lambda p: p in PUNCTUATION_CHARS
