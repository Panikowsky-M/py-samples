import os
from pprint import pprint as pp

def getHashes(git):
    
    subfolders = [f.path for f in os.scandir(d) if f.is_dir() ]
    subfolders.pop(58)
    subfolders.pop(25)
    objL = [] 
    _hash = []
    for i in subfolders:
        objL.append(str(i).replace('.git/objects/',''))
        _hash += os.listdir(i)
    fullHash = list(zip(objL,_hash))
    return fullHash


d = '.git/objects/'
pp(getHashes(d))
