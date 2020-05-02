PYBITES = "pybites"
text = "Aliquet nibh praesent tristique magna sit amet purus gravida quis"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    chars = list(PYBITES)
    result = ''.join([
        ''.join([char.swapcase()
                 if char and char.lower() in chars
                 else char
                 for char in word
                 ])
        for word in text])
    return result


print(convert_pybites_chars(text))
