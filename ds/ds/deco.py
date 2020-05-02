''' Testing principle behind itemgetter '''


def sampledeco(num):
    def decorator(iterable):
        return iterable[num]

    return decorator


l1 = [1, 2, 3, 4, 45, 5]

func1 = sampledeco(2)
print(func1(l1))
