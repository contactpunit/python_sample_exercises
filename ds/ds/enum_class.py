from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f'{self.name} => {THUMBS_UP * self.value}'

    @classmethod
    def average(cls):
        total = sum(level.value for level in cls)
        num = sum(1 for score in cls)
        return total / num


print(Score.average())
