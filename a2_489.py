import re
import operator

f = open('wiki_text.txt','rb')
text = str(f.readlines())
print(text)

words = re.findall('[a-zA-Z]+',text)

stats = {}
for w in words:
    stats[w] = stats.get(w,0) +1
print(stats)
