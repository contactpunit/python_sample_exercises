from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
if not os.path.exists(logfile):
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
        logfile
    )

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    datestring = line.split()[1]
    return datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S")



def time_between_shutdowns(loglines):
    """
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    required_lines = [line for line in loglines if 'Shutdown initiated' in line]
    first = convert_to_datetime(required_lines[0].strip())
    last = convert_to_datetime(required_lines[-1].strip())
    return last - first


time_between_shutdowns(loglines)