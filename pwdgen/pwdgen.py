#!/bin/python

import csv
import gzip
import string
import random
import secrets

DICE_COUNT = 5
dice_rolls = []
word_list = []

signs = ['</>','.','*^*','+','+=+','~>',';)',';(',':)',';(']

# Чтение csv-шек

with gzip.open('leetspeak.bin','rt') as f:
    ls_dict = dict(filter(None, csv.reader(f)))

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

with gzip.open('wordlist.bin','rt') as w:
    wrd = dict(filter(None, csv.reader(w)))
    for i in dice_rolls:
        for k, v in wrd.items():
            if i == k:
                word_list.append(v)

with gzip.open('scientist.bin','rt') as _s:
    sc = dict(filter(None, csv.reader(_s)))
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
