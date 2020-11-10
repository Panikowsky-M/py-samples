import os
from pprint import pprint as pp

def getHashes(git):
    
    subfolders = [f.path for f in os.scandir(d) if f.is_dir() ]
    INFO = subfolders.index('.git/objects/info')
    PACK = subfolders.index('.git/objects/pack')
    subfolders.pop(INFO)
    subfolders.pop(PACK)
    objL = [] 
    _hash = []
    for i in subfolders:
        objL.append(str(i).replace('.git/objects/',''))
        _hash.append(os.listdir(i))
    fullHash = dict(zip(objL,_hash))
    return fullHash


d = '.git/objects/'
objects = getHashes(d)

list1 = []
for i in objects.keys():
    list1.append(i)

list1 = sorted(list1)
list2 = []
list3 = []
for l in range(len(list1)):
    for m in range(len(objects.get(list1[l]))):
        list3.append('{}-> {}'.format(list1[l],objects.get(list1[l])[m] ))

pp(list3)
