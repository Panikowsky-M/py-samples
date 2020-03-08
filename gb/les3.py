import random
import time
yes = u'\u003D'
no  = u'\u003C'
no1 = u'\u003E'
print("Введите >,< или = для поиска числа.")
print(random.randint(1,100))
while True:
	x_input = input()
	if x_input == yes:
		break
	elif x_input == no:
		print(random.randint(1,100))
		time.sleep(1)
	elif x_input == no1:
		print(random.randint(1,100))
		time.sleep(1)
