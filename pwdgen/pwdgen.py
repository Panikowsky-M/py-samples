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

# Выбор длины пароля 


# Чтение csv-шек из архива

for m in tar.getmembers():
    file = tar.extractfile(m)
    filecontent.append(file.readlines())

ls_dict = dict(filter(None, csv.reader( codecs.iterdecode(filecontent[0],'utf-8') ) )  )

def cvrt_text(data):
    list_data = list(data)
    converted_data = []

    for i in list_data:
        converted_data += ls_dict[i]

    output_text = ''.join(converted_data)

    return output_text

for i in range(1,2):
  dice = ''.join(str(secrets.randbelow(6) + 1) for r in range(DICE_COUNT))
  dice_rolls.append(dice)

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
