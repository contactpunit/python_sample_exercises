from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
if not os.path.exists(COURSE_TIMES):
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
        COURSE_TIMES
    )


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as f:
        regex = '\d+:\d+'
        result = [re.findall(regex, line.strip())[0] for line in f if re.findall(regex, line.strip())]
        return result


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total = [
        timedelta(minutes=int(entry.split(':')[0]), seconds=int(entry.split(':')[1]))
        for entry in timestamps
    ]
    return str(sum(total, timedelta(0)))


# print(calc_total_course_duration(get_all_timestamps()))
