import pytest
from datetime import datetime
from ds.ds.heapq_largest import get_highest_earnings, get_largest_number, get_latest_dates


@pytest.mark.parametrize('numbers, n, expected', [
    ([6, 4, 5], 2, [6, 5]),
    ([6, 0, -3, 7, 9], 4, [9, 7, 6, 0])
])
def test_get_largest_number(numbers, n, expected):
    assert get_largest_number(numbers, n) == expected


@pytest.mark.parametrize('dates, n, expected', [
    (
            [datetime(2018, 1, 23, 0, 0),
             datetime(2017, 12, 19, 0, 0),
             datetime(2017, 10, 15, 0, 0),
             datetime(2019, 2, 27, 0, 0),
             datetime(2017, 3, 29, 0, 0),
             datetime(2018, 8, 11, 0, 0),
             datetime(2018, 5, 3, 0, 0),
             datetime(2018, 12, 19, 0, 0),
             datetime(2018, 11, 19, 0, 0),
             datetime(2017, 7, 7, 0, 0)], 2,
            [datetime(2019, 2, 27, 0, 0), datetime(2018, 12, 19, 0, 0)]
    )
])
def test_get_latest_dates(dates, n, expected):
    assert get_latest_dates(dates, n) == expected


@pytest.mark.parametrize('earnings_mln, n, expected', [
    ([
         {'name': 'Kevin Durant', 'earnings': 60.6},
         {'name': 'Adele', 'earnings': 69},
         {'name': 'Lionel Messi', 'earnings': 80},
         {'name': 'J.K. Rowling', 'earnings': 95},
         {'name': 'Elton John', 'earnings': 60},
         {'name': 'Chris Rock', 'earnings': 57},
         {'name': 'Justin Bieber', 'earnings': 83.5},
         {'name': 'Cristiano Ronaldo', 'earnings': 93},
         {'name': 'Beyoncé Knowles', 'earnings': 105},
         {'name': 'Jackie Chan', 'earnings': 49},
     ], 2, [{'name': 'Beyoncé Knowles', 'earnings': 105}, {'name': 'J.K. Rowling', 'earnings': 95}]
    ),
    ([
         {'name': 'Kevin Durant', 'earnings': 60.6},
         {'name': 'Adele', 'earnings': 69},
         {'name': 'Lionel Messi', 'earnings': 80},
         {'name': 'J.K. Rowling', 'earnings': 95},
         {'name': 'Elton John', 'earnings': 60},
         {'name': 'Chris Rock', 'earnings': 57},
         {'name': 'Justin Bieber', 'earnings': 83.5},
         {'name': 'Cristiano Ronaldo', 'earnings': 93},
         {'name': 'Beyoncé Knowles', 'earnings': 105},
         {'name': 'Jackie Chan', 'earnings': 49},
     ], 3, [{'name': 'Beyoncé Knowles', 'earnings': 105}, {'name': 'J.K. Rowling', 'earnings': 95},
            {'name': 'Cristiano Ronaldo', 'earnings': 93}
            ])
])
def test_get_highest_earnings(earnings_mln, n, expected):
    assert get_highest_earnings(earnings_mln, n) == expected
