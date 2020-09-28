import time
import string
import random
import base64

s1_signs = '!@#$%^&*()+=_-'
s0 = string.digits + string.ascii_letters + s1_signs
passwd = []
for i in range(0,15):
	passwd+= random.choice(s0)
	time.sleep(0)
result = ''
for i in passwd:
    result+= i 
passLen = len(result)
print("Сырой пароль: "+result + "\nдлина пароля: %d" % passLen)

base = result.encode("UTF-8")
enc = base64.b64encode(base)
b64pass = enc.decode("UTF-8")
print("\n--- \n"+"Закодированый в base64: "+b64pass)
passLen = len(b64pass)
print("Длина пароля: %d" % passLen)
