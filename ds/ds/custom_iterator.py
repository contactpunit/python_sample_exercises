from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return f'{choice(COLORS)} egg'
        else:
            raise StopIteration()
