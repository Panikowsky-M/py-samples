import json
from music_list import *

with open('songslist.json','w',encoding='utf-8') as myList:
    json.dump(fav_tracks,myList)

print('Структура была записана\
 в файл songslist.json\n')

print('Вот вывод структуры\
 в формате json\n')

d = open('songslist.json','r')
cat = d.readlines()
print(cat,'\n')
