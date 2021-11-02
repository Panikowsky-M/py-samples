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

def getObjects(o):
    _keys = []
    for i in o.keys():
        _keys.append(i)
    
    keysList = sorted(_keys)
    #list2 = []
    objectHashCodes = []
    for l in range(len(keysList)):
        for m in range(len(o.get(keysList[l]))):
            objectHashCodes.append('{}{}'.format(keysList[l],o.get(keysList[l])[m] ))

    return objectHashCodes

pp(getObjects(objects))

fullhashes = []
for n in getObjects(objects):
    os.system('git cat-file -t %s' % n)
