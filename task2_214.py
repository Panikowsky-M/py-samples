# Написать функцию check_passwandd, которая возвращает "valid", если пароль сильный,
# или "not valid", если это не так. Сильный пароль должен содержать от 8 до 20 символов
# латинского алфавита и хотя бы по одному символу из следующих категорий:
# прописные, строчные буквы, цифры и символы !@#$%^&*
#
# Пример:
# check_password("qwertYUI123##") ==> "valid"


import traceback 
import re
# import string


def check_password(password):
    mOb = re.match('[a-zA-Z0-9^\.]+',password)
    seOblowL = re.search('[a-z]+',password)
    seObupL = re.search('[A-Z]+',password)
    seObD = re.search('[0-9]+',password)
    if len(password) >= 8 and len(password) <= 20:
        #print(len(password))
        if mOb:
            if seOblowL and seObupL and seObD:
                return 'valid'
            else:
                return 'not valid'
        else:
             return 'not valid'
    else:
        return 'not valid'


#print(check_password("P1@pP1@pP1@pP1@pP1@pP1@p"))

# Тесты
try:
   assert check_password("") == "not valid"
   assert check_password("password") == "not valid"
   assert check_password("P1@p") == "not valid"
   assert check_password("P1@pP1@p") == "valid"
   assert check_password("P1@pP1@pP1@pP1@pP1@pP1@p") == "not valid"
   assert check_password("Paaaaaa222!!!") == "valid"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
