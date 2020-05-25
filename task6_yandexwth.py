import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.yandex.ru/weather/segment/details?\
offset=0&lat=55.753215&lon=37.622504&geoid=213&limit=10')
soup = bs(r.content,'lxml')
#print(soup)
weather = []
daily = {}

for card in soup.select('.card:not(.adv)'):
    date = ''.join([i.text for i in card.select('[class$=number],\
              [class$=month]')])

    temps = [i.text for i in card.select\
            ('.weather-table__body-cell_type_feels-like')]

    daypart = [i.text for i in card.select\
              ('.weather-table__daypart')]

    daily = dict(zip(daypart,temps))
    weather = [date,daily]
    print(weather)
    #,[i.text for i in card.select\
    #('.weather-table__body-cell_type_condition')]
    #.temp__value')],
    #[i.text for i in card.select\
    #('.weather-table__body-cell_type_humidity')]
    #,[i.text for i in card.select\
    #('.weather-table__body-cell_type_air-pressure')]
    #))
