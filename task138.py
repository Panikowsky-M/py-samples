# Написать функцию balanced_num, которая определяет является ли заданное число
# сбалансированным, т.е.
# сумма цифр справа и слева от середины равны (abcde ==> a + b == d + e; abcdef
# ==> a + b == e + f)
#
# Примеры:
# balanced_num(2222) ==> True
# balanced_num(135622) ==> True

import traceback
#from math import log10, ceil

def _count(num):
    res,n = 0, int(num)
    while n > 0:
        res += n%10 #1
        n //= 10
    return res
    
def balanced_num(num):
     num_str = str(num)
     mid_idx = len(num_str)//2
     if mid_idx <= 1:
        return True

     if len(num_str) % 2 == 1:
        countLeft = _count(num_str[:mid_idx]) 
        countRight = _count(num_str[mid_idx+1:])
     else:
        countLeft = _count(num_str[:mid_idx-1]) 
        countRight = _count(num_str[mid_idx+1:])
     return countLeft == countRight

#def balanced_num(num):
#    num_l = ceil(log10(num))
#    leftS = num // 10 ** (num_l // 2 + num_l %2)
#    rightS = num % (10 ** (num_l // 2))
#    return (_count(leftS) == _count(rightS))

#print('4251 is ', balanced_num(4251))
#print('2222 is ',balanced_num(2222))
#print('135622 is ',balanced_num(135622))
#print('56239814 is ', balanced_num(56239814))
#print('13 is',balanced_num(13))
#print('295591 is',balanced_num(295591))
#print('1230987 is',balanced_num(1230987))
#print('0 is ',balanced_num(0))

# Тесты
try:
    assert balanced_num(13) == True
    assert balanced_num(0) == True
    assert balanced_num(295591) == False
    assert balanced_num(56239814) == True
    assert balanced_num(1230987) == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
