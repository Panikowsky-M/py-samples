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
            return el

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


listAll(library)
x_in = int(input('Вводите года/номера для поиска\n'))
#print(outByNums(x_in,library))
#outNumOfElders(x_in,library)
#print(listAll(library))
print(Refresh(x_in,library))
listAll(library)
#x_in = int(input())
#print(outByYear(x_in,library))
