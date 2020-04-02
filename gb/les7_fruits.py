fr0 = ['груша','яблоко','банан','личи','киви','айва','дыня']
fr1 = ['груша','яблоко','банан','апельсин','грейпфрут','манго']
fr2 = 123 
def sl0_get(l1,l2):
    res = []
    try:
        res = [i for i in l1 if i in l2 ]
    except Exception as e1:
        print('Ошибка: ', e1)
    return res

print(sl0_get(fr0,fr1))
print(sl0_get(fr0,fr2))
