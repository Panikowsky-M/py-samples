import re

f = open('wiki_text.txt','r')
text = str(f.readlines())
print("%s\n" % text)

words = re.findall('[a-zA-Z]+',text)
print("%s\n" % words)

stats = {}
for w in words:
    stats[w] = stats.get(w,0) + 1

print(stats)
