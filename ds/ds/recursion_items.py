def pairs(iterator):
    def pair_from(head, iterable_nxt):
        try:
            nxt = next(iterable_nxt)
            yield head, nxt
            yield from pair_from(nxt, iterable_nxt)
        except StopIteration:
            return
    try:
        b = pair_from(next(iterator), iterator)
        return b
    except StopIteration:
        return


a = iter([1, 2, 6, 4, 5, 3, 7])
b = pairs(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
