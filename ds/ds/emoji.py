import re
from typing import List
import emojis

text = "We see more and more 🐍 Python 🥋 ninjas, keep it up 💪"
IS_EMOJI = re.compile(r'[^\w\s,]')


# TODO: complete function
def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    final = []
    for word in text.split():
        if word.startswith('\\U'):
            final.append(text.index(word))
    return final


print(get_emoji_indices(text))

# text.index(word)gc_conten
# if emojis.decode(word).startswith(':')
