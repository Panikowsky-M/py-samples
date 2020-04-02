import math

nl0 = [49,64,32,81,121,256]
nl1 = ['q','w','t','a']

def sroot(x):
    res = []
    try:
        res = [j if j <= 0 else math.sqrt(j) for j in x]
    except Exception as e1:
        print('Ошибка:',e1)
    return res
print(sroot(nl0))
print(sroot(nl1))
