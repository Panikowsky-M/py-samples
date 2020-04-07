import os, shutil, datetime,time

def newCD(x):
    if os.path.isdir(x):
        try:
            print(os.getcwd())
            os.chdir(path)
            print(os.getcwd())
        except FileNotFoundError:
            print('Папка не найдена')
    else:
        print('Параметр передан неверно')

def newCP(x0,x):
    if os.path.isdir(x0):
        try:
            shutil.copytree(x0,x)
        except FileExistsError:
            print('Папка существует')
    else:
        try:
            shutil.copy(x0,x)
        except FileNotFoundError:
            print('Файл не найден')

def newLS(folders_only=False):
    res = os.listdir()
    if folders_only:
        res = [f for f in result if os.path.isdir(f)]
    print(res)
def Touch(x, text=None):
    with open(x, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def newRM(x):
    if os.path.isdir(x):
        os.rmdir(x)
    else:
        try:
            os.remove(x)
        except FileNotFoundError:
            print('Файл не найден')
            
def Mkdir(x):
    try:
        os.mkdir(x)
    except FileExistsError:
        print('Папка существует')

def _WriteLog(text):
    boardTime = datetime.datetime.now()
    boardTimeUnix = round(boardTime.timestamp(),1)
    res = f'{boardTimeUnix} - {text}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(res + '\n')


if __name__ == '__main__':
    Touch('touch_test.txt')
    Mkdir('clear-dir')
    newLS()

    newCP('touch_test.txt', 'touch_copy.txt')
    newCP('clear-dir', 'clear-copy')
    newLS()

    newRM('touch_test.txt')
    newRM('clear-dir')
    newRM('touch_copy.txt')
    newRM('clear-copy')
    newLS()
