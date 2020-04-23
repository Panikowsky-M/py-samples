import re

f = open('wiki_text.txt','r')
text = str(f.readlines())
print("%s\n" % text)

words = re.findall('[a-zA-Z]+',text)
#print("%s\n" % words)

stats = {}
for w in words:
    stats[w] = stats.get(w,0) + 1

w_ranks = sorted(stats.items(), key = lambda x : x[1],\
      reverse=True) [:10]
_wrex = re.findall('[a-zA-Z]+',str(w_ranks))
_drex = re.findall('[0-9]+',str(w_ranks))
pl = [p for p in range(1,10)]
for j in range(len(_wrex)-1):
    places = '{} place,{} - {} times'.format(pl[j],_wrex[j],_drex[j])
    print(places) 
