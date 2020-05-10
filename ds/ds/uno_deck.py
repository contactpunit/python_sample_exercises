from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    names = [i for i in range(1, 10) for _ in range(2)]
    names.extend(i for i in ('Draw Two', 'Skip', 'Reverse') for _ in range(2))
    names.extend([0])
    cards = [UnoCard(suit=suit, name=name) for name in names for suit in SUITS]
    cards.extend([UnoCard(suit=None, name=name) for name in ('Wild', 'Wild Draw Four') for _ in range(4)])
    return cards

 # cards.extend([UnoCard(suit=suit, name=name) for name in ('Wild', 'Wild Draw Four') for suit in SUITS])


print(create_uno_deck())
