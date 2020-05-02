from itertools import combinations


def find_number_pairs(numbers, N=10):
    return [c for c in combinations(numbers, 2) if sum(c) == N]


print(find_number_pairs([2, 3, 5, 4, 6]))
