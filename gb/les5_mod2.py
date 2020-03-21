import random

def rEl(inp_l):
	c0 = -1
	if len(inp_l) == 0:
		return None
		print("Код возврата %d пустой список на входе!" % c0)
	else :
		return random.choice(inp_l)
		c0+=1
		print("Код возврата %d модуль работает в штатном режиме..." % c0)
#city_list = ["Москва","Краснодар","Новосибирск","Калуга"]
#city_list = []
#print(rEl(city_list))
