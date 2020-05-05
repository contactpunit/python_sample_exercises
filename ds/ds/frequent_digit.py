from collections import Counter

def freq_digit(num: int) -> int:
    c = Counter(str(num))
    return int(c.most_common(1)[0][0])

print(freq_digit(2020))