import pickle
from music_list import *

with open('songslist.dat','wb') as file:

    pickle.dump(fav_tracks,file)

print('Структура была записана\
 в файл: songslist.dat\n')

print('Вот вывод записанной\
 структуры в формате pickle\n')

d = open('songslist.dat','rb')
cat = d.readlines()
print(cat,'\n')
