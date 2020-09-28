import time
import string
import random
import base64

lowRange = 0
highRange = int(input("Введите длину пароля: "))
s1_signs = '!@#$%^&*()+=_-'
s0 = string.digits + string.ascii_letters + s1_signs
passwd = []
for i in range(0,30):
	passwd+= random.choice(s0)
	time.sleep(0)
passwd=passwd[lowRange:highRange]

result=''
for i in passwd:
    result+= i

passLen = len(result)
print("Сырой пароль: "+result + "\nдлина пароля: %d" % passLen)
passwd = []

base = result.encode("UTF-8")
enc = base64.b64encode(base)
b64pass = enc.decode("UTF-8")
passwd+=b64pass
passwd=passwd[lowRange:highRange]

result=''
for i in passwd:
    result+= i

print("\n--- \n"+"Закодированый в base64: "+result)
passLen = len(result)
print("Длина пароля: %d" % passLen)
