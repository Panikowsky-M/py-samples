import urllib
import requests
from bs4 import BeautifulSoup

MyURL = 'http://coronavirusstat.ru/country/russia'

page = urllib.urlopen(MyURL)
print(page.status_code)

soup = BeautifulSoup(page)
inf = soup.findAll('thead')
print(inf)
