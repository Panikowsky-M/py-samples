num = input('Введите число:')
#e0 = 0

def q1(x):
    try:
        y = int(x)
        if y == 13:
            raise ValueError("13 - недопустимое число!\n")
            #e0 += 1
        res = y**2
    except Exception as e1:
        print('Ошибка:',e1)
    else:
        return res
print(q1(num))
