import sys
from l8_mgr import _WriteLog,newLS,newCP,newRM,Touch,Mkdir,newCD
from l8_g import RunGame 

print('Внимание, именна команд названы в стиле UNIX!\n\
Для справки вызовите \'help\'\n')
_WriteLog('Модуль запущен')

try:
    command = sys.argv[1]
except IndexError:
    _WriteLog('11:Вызов исключения,пустая комманда')
    print('Вы не ввели команду!')
else:
    if command == 'ls':
        newLS()
        _WriteLog('Вывод списка файлов...')
    elif command == 'touch':
        try:
            name = sys.argv[2]
        except IndexError:
            _WriteLog('20:Исключение, пустое имя файла')
            print('Пустое имя файла')
        else:
            if len(sys.argv) == 4:
                text = sys.argv[3]
                Touch(name, text)
            else:
                Touch(name)
    elif command == 'mkdir':
        try:
            name = sys.argv[2]
        except IndexError:
            _WriteLog('33:Исключение, пустое имя папки')
            print('Нечего создавать')
        else:
            Mkdir(name)
    elif command == 'rm':
        try:
            name = sys.argv[2]
        except IndexError:
            _WriteLog('41:Исключение, пустое имя')
            print('Нечего удалять')
        else:
            newRM(name)
    elif command == 'cp':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            if len(sys.argv) == 3:
                _WriteLog('50:Исключение,не могу копировать без цели')
                print('Нечего копировать')
            else:
                _WriteLog('54:Не могу копировать без пути')
                print('Нечего копировать')
        else:
            newCP(name, new_name)
    elif command == 'cd':
        try:
            path = sys.argv[2]
        except IndexError:
            _WriteLog('62:Не могу ходить без пути')
            print('Не дано имя папки')
        else:
            newCD(path)
    elif command == 'game':
        RunGame()
    elif command == 'help':
        print('ls - список файлок и папок')
        print('touch - создание файла')
        print('mkdir - создание папки')
        print('rm - удаление файла или папки')
        print('cp - копирование файла или папки')
        print('cd - сменить текущую папку')
        print('game - игра')

_WriteLog('Модуль завершил работу')
