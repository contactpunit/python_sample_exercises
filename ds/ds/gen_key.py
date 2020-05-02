import random, string


def gen_key(parts=4, chars_per_part=8):
    return '-'.join(
        [
            ''.join(
                [
                    random.choice(string.digits + string.ascii_letters.upper())
                    for char in range(chars_per_part)
                ]
            )
            for part in range(parts)
        ]
    )


print(gen_key(parts=3, chars_per_part=4))
