"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. 
  (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, 
  как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для 
  подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя метод format
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке 
  записывать не более 100 символов и не делить слова.
"""

def wiki_function():
    # Тело функции
    return 1


# Вызов функции
wiki_function()
