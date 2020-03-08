a = int(input())
t = 0
word = "Is not power of 2"
if a%2 == 0 :
	while a>=2:
		a=a//2
		t+=1
	print(t)
else:
	print(word)
