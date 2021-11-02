import re

x = str(input()) 

if (re.search('\d{4}[а-я]',x)):
   print("Это военный номер.")
if (re.search('[а-я]\d{3}[а-я]{2}',x)):
   print("Это гражданский номер")
