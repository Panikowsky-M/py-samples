# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# + вывода информации о всех книгах;
# + вывода информации о книге по введенному с клавиатуры номеру;
# + вывода количества книг, старше введённого года;
# – обновлении всей информации о книге по введенному номеру;
# + удалении книги по номеру.
# Провести тестирование функций.

library = [{"id": 12,\
            "title" : "В интересах революции",\
            "group" : "Агата Кристи",\
            "year" : 2004},\
            {"id": 13,\
            "title": "Серебро",\
            "group":"Би-2",\
            "year": 2000},\
            {"id":14,\
            "title": "Люди на холме",\
            "group":"Наутилус Помпилиус",\
            "year": 1986},\
            {"id": 15,\
            "title" : "Uselink",\
            "group": "Depeche Mode",\
            "year": 1997}]

def listAll(lib):
    for i in range(len(lib)):
        el = '{},{},{},{}'\
             .format( lib[i].get('id'),\
                      lib[i].get('title'),\
                      lib[i].get('group'),\
                      lib[i].get('year'))
        print("%s\n"% el) 

def outByNums(x,lib):
    for i,el in enumerate(lib):  #Сокращает проход по списку с трех до двух
        if x is el['id']:        #строк кода
            el2 = '{},{},{},{}'\
                  .format( lib[i].get('id'),\
                  lib[i].get('title'),\
                  lib[i].get('group'),\
                  lib[i].get('year'))
    return el2

def popByNums(x,lib):
    for i,el in enumerate(lib): 
        if x is el['id']:
            lib.pop(i)
            return el

def outByYear(x,lib):
    c = 0 
    for i,el in enumerate(lib): 
        if x < el['year']:
            c+=1   
    print(c)


#listAll(library)
x_in = int(input('Вводите года для поиска\n'))
#print(outByNums(x_in,library))
outByYear(x_in,library)
#print(listAll(library))

#x_in = int(input())
#print(outByYear(x_in,library))
