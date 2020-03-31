import re

def Delbs(f_name,pattL):
	newList = []
	with open(f_name,'r') as file:
		text = " ".join([x.strip("\n") for x in file.readlines()])
	for patt in pattL:
		newList.append(patt)
	return set(newList)
text = open('wiki_text.txt','r')
rdL = str(text.readlines())
p = re.findall('\w+',rdL)
print(Delbs('wiki_text.txt',p))
