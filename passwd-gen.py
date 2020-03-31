import time
import string
import random

s1_signs = '!@#$%^&*()+=_-'
s0 = string.digits + string.ascii_letters + s1_signs
passwd = []
n = int(input())
for i in range(0,n):
	passwd+= random.choice(s0)
	time.sleep(0)
print(str(passwd))
