names = ['schwarzenegger arnold',
         'baldwin alec',
         'belderbos bob',
         'sequeira julian',
         'bullock sandra',
         'reeves keanu',
         'pybites julbob',
         'belderbos bob',
         'sequeira julian',
         'pacino al',
         'pitt brad',
         'damon matt',
         'pitt brad']


def _helper(name):
    fname, lname = name.split()
    return ' '.join((lname, fname))


final = [_helper(name) for name in names]

# using generators
import random


def gen_pairs():
    first_names = [name.split()[0] for name in names]
    while True:
        fname, lname = None, None
        while fname == lname:
            fname, lname = random.sample(first_names, 2)
        yield f'{fname} teams with {lname}'


gen = gen_pairs()
for _ in range(10):
    print(next(gen))
