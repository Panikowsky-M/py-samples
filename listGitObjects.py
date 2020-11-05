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
pp(objects.get('77'))
