hs = ['02',2,'02',2,2,2,2]
ms = [15,47,17,32,17,22,31]
ss = [59,16,20,34,17,'00',41] 

tmp = []
avg = []
rng = []

def myStat(x,y,y1):
    IntX = []
    for i in range(len(x)):
        IntX.append(int(x[i]))
    print("Массив целых на входе:%s\n" % IntX)
    M = max(IntX) 
    m = min(IntX)
    ran0 = M-m
    avg0 = round( sum(IntX)/len(IntX) ) 
    y.append(ran0)
    y1.append(avg0)
    return y,y1 

print(myStat(hs,tmp,avg))
print(myStat(ms,tmp,avg))
print(myStat(ss,tmp,avg))
