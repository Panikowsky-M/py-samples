import traceback

def balanced_num(number):
	p_left = (number - 1)
	p_right = (number + 1)
	p_n = (p_left + p_right)/2
	return True


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
