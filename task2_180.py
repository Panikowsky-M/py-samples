# Написать функцию longest, которая возвращает наибольшую по длине подстроку подряд идущих символов,
# расставленных в алфавитном порядке
#
# Примеры:
# longest("zadfaa") ==> "adf"

import traceback


def longest(s):
    # Тело функции
    return ""


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
