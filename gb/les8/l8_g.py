import random,datetime,time

def RunGame():
    print('Так как вы ввели команду \'game\', то давайте сыграем в игру')
    print('Вводите >,< или = для выбора числа\n') 
    input('Загадайте целое число от 1 до 100 и нажмите Return ')

    m = 1
    M = 100
    ans = None
    rng = False

    Now = datetime.datetime.today()
    UnixNow = Now.timestamp()
    deltaL = 1 - round(1000000/UnixNow,4)
    deltaR = 1 + round(1000000/UnixNow,4)
    doubleside = [deltaL,deltaR]
    
    while ans != '=':
        num = random.randint(m,M)
        ans = input('Загаданное число %d ?' %num)
        if ans == '>':
            if num == 100:
                print('Загаданное число лежит вне диапазона')
                rng = True
            m = round(num + random.choice(doubleside) )

        elif ans == '<':
            if num == 1:
                print('Загаданное число лежит вне диапазона')
                clear_range = True
            M = round(  num - random.choice(doubleside) )
        if M < m or m > M or rng:
            print('Давайте попробуем заново, загадайте любое число от 1 до 100')
            m = 1
            M = 100
            rng = False

    print('Число было удачно подобрано')


