import os
import sys

def rmd():
	name ='dir'
	c = -1
	for i in range(1,10):
		newD = os.path.join(os.getcwd(),'{}_{}'.format(name,i))
		os.mkdir(newD)
		print("Создана папка %s" % newD)
		c+=1
	if c >= 0:
		print("Код возврата %d\n модуль работает в штатном режиме!" % c)
	#return c
	else:
	#return c
		print("Код возврата %d\n Модуль работает в нештатном режиме!" % c) 
