while True:
    num = int(input('Введите число: '))
    if num > 0 and num < 10:
        print(num**2)
        break
    else:
        print('Число должно находиться от 0 до 10') 
