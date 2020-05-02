from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    sdate = PYBITES_BORN
    hday = sdate + timedelta(days=100)
    yday = sdate + timedelta(days=365)
    while True:
        if hday > yday:
            yield yday
            sdate = yday
            yday = sdate + timedelta(days=365)
        elif yday > hday:
            yield hday
            sdate = hday
            hday = sdate + timedelta(days=100)


g = gen_special_pybites_dates()
for d in range(5):
    print(next(g))

gen_special_pybites_dates()
