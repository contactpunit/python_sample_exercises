chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    result = ''.join(['' if char in chars else char for char in input_string])
    return result


print(remove_punctuation('i am a boy'))
