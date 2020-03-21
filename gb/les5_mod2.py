import random

def rEl(inp_l):
	if len(inp_l) == 0:
		return None
	else :
		return random.choice(inp_l)
#city_list = ["Москва","Краснодар","Новосибирск","Калуга"]
#city_list = []
#print(rEl(city_list))
