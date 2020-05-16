import bisect

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = zip(scores, belts)


def get_belt(user_score):
    if user_score < 10:
        return None
    position = bisect.bisect(scores, user_score)
    return belts[position - 1]
