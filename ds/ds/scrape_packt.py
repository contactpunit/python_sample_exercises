from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    # print(soup.prettify())
    raw_title = soup.find_all('div', class_="dotd-main-book-summary")
    title = raw_title[0].find('h2').text.strip()
    description = raw_title[0].find_all('div')[2].text.strip()
    img = soup.find_all('img', class_="bookimage")[0]['src']
    p = soup.find_all('div', class_="dotd-main-book-image float-left")
    link = p[0].find('a')['href']
    return Book(title=title, description=description, image=img, link=link)





get_book()
