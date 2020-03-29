import pickle
fav_tracks = [
    {'name':'В интересах революции','artist': 'Агата Кристи'},
    {'name':'Деньги на ветер','artist': 'Би-2'},
    {'name':'Земля','artist': 'Маша и Медведи'},
]

with open('songslist.dat','wb') as file:

    pickle.dump(fav_tracks,file)

print('Структура была записана\
 в файл: songslist.dat\n')

print('Вот вывод записанной\
 структуры в формате pickle\n')

d = open('songslist.dat','rb')
cat = d.readlines()
print(cat,'\n')

