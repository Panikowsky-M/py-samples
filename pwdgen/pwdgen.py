#!/bin/python

import csv
import codecs
import random
import secrets
import tarfile

AR = 'words.dat'
tar = tarfile.open(AR)
DICE_COUNT = 5
dice_rolls = []
word_list = []
filecontent = []

signs = ['</>','.','*^*','+','+=+','~>',';)',';(',':)',';(']

print('''
      \033[01;33mГенеретор паролей по методу игральных костей\033[0m\n
      Генератор подбрасывает кубики и выбирает слово из словаря, которое
      соответсвует выпавшему числу. Полученная комбинация слов переводится
      в особый алфавит, что придает паролю большую стойкость.\n
      Более подробно в источнике:\n
      https://theworld.com/~reinhold/diceware.html#Diceware%20in%20Other%20Languages%7Coutline
      ''')

# Выбор длины пароля 

while True:
    try:
        pwd_lenght = int(input('Выберите количество костей для генерации пароля (Рекомендовано как минимум 6): '))
        val = int(pwd_lenght)
        if val > 0:
            break
        else:
            print("\nЧисло не может быть 0 или отрицательным\n")
            continue
    except ValueError:
        print("\nВообще-то на вход поступают числа !\n")
        continue


# Чтение csv-шек из архива

for m in tar.getmembers():
    file = tar.extractfile(m)
    filecontent.append(file.readlines())

ls_dict = dict(filter(None, csv.reader( codecs.iterdecode(filecontent[0],'utf-8') ) )  )

# Перевод нормальных слов в c001haxXx0rZz_sp34c4

def cvrt_text(data):
    list_data = list(data)
    converted_data = []

    for i in list_data:
        converted_data += ls_dict[i]

    output_text = ''.join(converted_data)

    return output_text

# Бросание костей 

for i in range(pwd_lenght):
  dice = ''.join(str(secrets.randbelow(6) + 1) for r in range(DICE_COUNT))
  dice_rolls.append(dice)

# Заполнение итоговой строки 

wrd = dict(filter(None, csv.reader(codecs.iterdecode(filecontent[2],'utf-8')) ))  
for i in dice_rolls:
  for k, v in wrd.items():
    if i == k:
     word_list.append(v)

sc = dict(filter(None, csv.reader(codecs.iterdecode(filecontent[1],'utf-8')) )) 
for i in dice_rolls:
  for k, v in sc.items():
      if i == k:
          word_list.append(v)

print('\n- Выбор слов был таким: -\n')
for i in word_list:
    print(i, end=' ')

final_passphrase = " ".join(word_list).replace(" ", "_")

print('\n\n- Ваш пароль стал таким: -\n')

print( str(random.choice(signs) + cvrt_text(final_passphrase) + str(random.choice(signs)) ) )
