from collections import namedtuple
from datetime import datetime, timedelta
from bisect import bisect

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2 * MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2 * HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2 * DAY, 'yesterday', None),
)

t_offsets = [t.offset for t in TIME_OFFSETS]


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    try:
        if date > NOW:
            raise ValueError()
        final_date = NOW - date
        total_seconds = (NOW - date).total_seconds()
        i = bisect(t_offsets, total_seconds)
        try:
            result = TIME_OFFSETS[i].date_str
            if '{}' in result:
                if 'seconds' in result:
                    return result.format(int(total_seconds))
                elif 'minutes' in result:
                    return result.format(int(total_seconds/MINUTE))
                elif 'hours' in result:
                    return result.format(int(total_seconds/HOUR))
                else:
                    return result
            else:
                return result
        except IndexError:
            req_date = datetime.now() - final_date
            # return f'{req_date.month}/{req_date.day}/{req_date.year}'
            return req_date.strftime('%m/%d/%y')
    except TypeError:
        raise ValueError()


print(pretty_date(NOW + timedelta(days=1)))
# print(pretty_date(NOW - timedelta(hours=48)))
# print(pretty_date(datetime(2019, 6, 24, 3, 15, 11, 637276)))
# print(pretty_date(datetime(2020, 7, 7, 3, 48, 57, 461313)))
