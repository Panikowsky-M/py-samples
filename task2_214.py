# Написать функцию check_passwandd, которая возвращает "valid", если пароль сильный,
# или "not valid", если это не так. Сильный пароль должен содержать от 8 до 20 символов
# латинского алфавита и хотя бы по одному символу из следующих категорий:
# прописные, строчные буквы, цифры и символы !@#$%^&*
#
# Пример:
# check_password("qwertYUI123##") ==> "valid"


import traceback 
import re


def check_password(password):
	ok = "valid"
	error = "not valid"
	v = -5
	l = len(password)
	if l >= 8:
		v+=1
		if l <= 20:
			v+=1
			if(re.search('[a-zA-z]',password)):
				v+=1
				if (re.search('[0-9]',password)):
					v+=1
					if (re.search('[!@#$%^&*_,.:;]',password)):
						v+=1
	if v == 0:
		return ok
	else: return error

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
