import csv
from collections import defaultdict
import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    data = requests.get(CSV_URL)
    if data.status_code == 200:
        return data.text


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    d = defaultdict(int)
    reader = csv.DictReader(content.split('\n'))
    for row in reader:
        d[row['tz']] += 1
    for k, v in d.items():
        print(f'{k:<21}| {"+" * v}')


# get_csv()
create_user_bar_chart(get_csv())
