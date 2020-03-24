# Написать функцию order_weight, которая сортирует список положительных чисел.
# Критерий сортировки - возрастание веса числа (сумма всех цифр числа).
# Если два числа имеют одинаковый вес, сортировать их так, словно они строки.
#
# Примеры:
# [56, 65, 74, 100, 99, 68, 86, 180, 90] ==>
# [100, 180, 90, 56, 65, 74, 68, 86, 99]


import traceback


num_weight = lambda x: sum(int(i) for i in str(x))

def order_weight(integers):
    for i in range(len(integers)-1):
        if num_weight(integers[i]) < num_weight(integers[i+1]):
            integers.sort(key=num_weight)
        elif num_weight(integers[i]) == num_weight(integers[i+1]):
            integers.sort()
    print(integers)
    return integers


# Тесты
try:
    assert order_weight([103, 123, 4444, 99, 2000]) == [2000, 103, 123, 4444, 99]
    assert order_weight([2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]) == [11, 11, 2000, 10003, 22, 123, 1234000, 44444444, 9999]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
