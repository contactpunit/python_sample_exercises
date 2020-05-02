class Hand:
    def __init__(self, one_card, *cards):
        self.one_card = one_card
        self.cards = list(cards)

    def __str__(self):
        return ', '.join(c for c in self.cards)

    def __repr__(self):
        return ', '.join(map(repr, self.cards))


h = Hand('one', '1', '2', '3')
print(h)

