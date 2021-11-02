# Написать функцию longest, которая возвращает наибольшую по длине подстроку 
# подряд идущих символов,
# расставленных в алфавитном порядке
#
# Примеры:
# longest("zadfaa") ==> "adf"

import traceback

def longest(s,key=lambda x: x):
    max_st  = 0
    max_len = 0
    cur_len = 1
    cur_st  = 0

    for i in range(1,len(s)):
        if key(s[i-1]) <= key(s[i]):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                max_st = cur_st
            cur_st = i
            cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
        max_st  = cur_st

    return s[max_st:max_st+max_len]


# Тесты
try:
    assert longest('asd') == 'as'
    assert longest('nab') == 'ab'
    assert longest('abcdeapbcdef') == 'abcde'
    assert longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt'
    assert longest('asdfbyfgiklag') == 'fgikl'
    assert longest('zyba') == 'z'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
