import calendar, datetime

mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    return mapping.get(calendar.weekday(date.year, date.month, date.day), None)


dt = datetime.date(1974, 11, 11)
weekday_of_birth_date(dt)
