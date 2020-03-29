import pickle, json

with open('songslist.json', 'r', encoding='utf-8') as file:
     tracks = json.load(file)

print('В файле обнаружена структура\
 в формате json\n')

print('Вывод структуры:\n %s\n' % tracks)
with open('songslist.dat', 'rb') as file0:
    tracklist = pickle.load(file0)

print('В файле обнаружена структура\
 в формате pickle\n')

print('Вывод структуры:\n %s' % tracklist)
