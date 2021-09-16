import requests as rq
from bs4 import BeautifulSoup as BS4

# site = rq.get("https://en.wikipedia.org/wiki/List_of_Russian_scientists")
site = rq.get("https://en.wikipedia.org/wiki/List_of_American_artists_1900_and_after")
soup = BS4(site.text)
# print(soup)

texts = []
div = soup.find('div',{'class':'mw-parser-output'})
dots = div.find_all('li')
for punct in dots:
  title = punct.find('a').get('title')
  texts.append(title)

# del texts[652:841]
# del texts[-1]
# del texts[-1]

with open('scientists.txt','w',encoding='utf-8') as f:
 for l in texts:
   print(l,file=f) 
