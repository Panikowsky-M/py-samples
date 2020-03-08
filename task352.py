# Банкомат содержит достаточное количество банкнот номиналом
# 50, 100, 200, 500, 1000, 2000, 5000 рублей.
# Написать функцию atm, которая определяет наименьшее количество купюр
# выдачи для запрашиваемой суммы или выдает -1 при невозможности выдачи такой суммы
#
# Пример
# atm(7700) ==> 4 ( 1 x 5000, 1 x 2000, 1 x 500, 1 x 200)


import traceback


def atm(money):
    # Тело функции
    return 0


# Тесты
try:
    assert atm(7700) == 4
    assert atm(1255) == -1
    assert atm(13650) == 7
    assert atm(1000) == 1
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
