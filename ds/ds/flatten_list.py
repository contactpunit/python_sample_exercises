# result = []


def flatten(l_of_lists):
    for item in l_of_lists:
        if item.__class__.__name__ in ['str', 'int']:
            yield item
            # result.append(item)
        else:
            yield from flatten(item)
