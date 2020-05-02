# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# + вывода информации о всех книгах;
# + вывода информации о книге по введенному с клавиатуры номеру;
# + вывода количества книг, старше введённого года;
# + обновлении всей информации о книге по введенному номеру;
# + удалении книги по номеру.
# Провести тестирование функций.

#import re

library = [{"id": 12,\
            "title" : "В интересах революции",\
            "album" : "???",\
            "group" : "Агата Кристи",\
            "year" : 2004},\
            {"id": 13,\
            "title": "Серебро",\
            "album": "Би-2(2000)",\
            "group":"Би-2",\
            "year": 2000},\
            {"id":14,\
            "title": "Люди на холме",\
            "album": "Яблокитай",\
            "group":"Наутилус Помпилиус",\
            "year": 1986},\
            {"id": 15,\
            "title" : "Uselink",\
            "album" : "Ultra",\
            "group": "Depeche Mode",\
            "year": 1997},\
            {"id": 16,\
            "title" :"Home",\
            "album" : "Ultra",\
            "group" : "Depeche Mode",\
            "year" : 1997},\
            {"id": 17,\
            "title" : "Enjoy The Silence",\
            "album" : "Violator",\
            "group" : "Depeche Mode",\
            "year" : 1990},\
            {"id": 18,\
            "title" : "Policy Of True",\
            "album" : "Violator",\
            "group" : "Depeche Mode",\
            "year" : 1990},\
            {"id": 19,\
            "title": "У меня нет дома",\
            "album" : "##Сингл##",\
            "group" : "Один в каное",\
            "year" : 2019},\
            {"id": 20,\
            "title": "Кавачай",\
            "album" : "Глория",\
            "group" : "Океан Ельзы",\
            "year" : 2005},\
            {"id": 21,\
            "title": "Скользкие улицы",\
            "album" : "Иномарки",\
            "group" : "Би-2",\
            "year" : 2004},\
            {"id": 22,\
            "title": "Секрет",\
            "album" : "Майн кайф?",\
            "group" : "Агата Кристи",\
            "year" : 2000}
            ]

def listAll(lib):
    for i in range(len(lib)):
        el = '{}: {} ->{} ->{} ->{}'\
             .format( lib[i].get('id'),\
                      lib[i].get('title'),\
                      lib[i].get('album'),\
                      lib[i].get('group'),\
                      lib[i].get('year'))
        print("%s\n"% el) 

def outByNums(x,lib):
    for i,el in enumerate(lib):  #Сокращает проход по списку с трех до двух
        if x is el['id']:        #строк кода
            el2 = '{}: {} ->{} ->{} ->{}'\
                  .format( lib[i].get('id'),\
                  lib[i].get('title'),\
                  lib[i].get('album'),\
                  lib[i].get('group'),\
                  lib[i].get('year'))
    return el2

def popByNums(x,lib):
    for i,el in enumerate(lib): 
        if x is el['id']:
            lib.pop(i)
            print('Удалено!\n')
            return el['id']

def outNumOfElders(x,lib):
    c = 0 
    for i,el in enumerate(lib): 
        if x > el['year']:
            c+=1   
    print("%d песен старше введеного года \n"%c)

def Refresh(x,lib):
   for i,el in enumerate(lib):
    if x is el['id']:
            lib[i].update({'title':input('Введите название: '),\
                  'album':input('Введите альбом: '),\
                  'group':input('Введите группу: '),\
                  'year':int(input('Введите год: '))})
            el2 = '{} ->{} ->{} ->{}'\
                  .format( lib[i].get('title'),\
                           lib[i].get('album'),\
                           lib[i].get('group'),\
                           lib[i].get('year'))
   return el2 

x = int(input('Вводите номера от 12 до 22: '))
Refresh(x,library)
listAll(library)
popByNums(x,library)
outNumOfElders(2004,library)
listAll(library)

#s = '' 
#if x_in  == 'all':
#    s = 'listAll(library)'
#    eval(s)
#elif x_in  == 'ref':
#     n = int(input('Введите номер ячейки: \n'))
#     s = 'Refresh(n,library)'
#     eval(s)
#     listAll(library)
#
#if re.findall('[pop]?\d{2}',x_in):
#    X = re.split('[a-z]+',x_in)
#    n = int(X[1])
#    s = 'print(popByNums(n,library))'
#    eval(s)
#    print('\n')
#    listAll(library)
#
#if re.findall('[a-z]+?\d{2,}?',x_in):
#    #X = re.split('[a-z]+',x_in)
#    n = int(x_in)
#    s = 'print(outByNums(n,library))'
#    eval(s)
#    if re.findall('[year]?\d{4}',x_in):
#        X = re.split('[a-z]+',x_in)
#        n = int(X[1])
#    s = 'outNumOfElders(n,library)'
#    eval(s)
