ls = [2000,10003,1234000,44444444,9999,11,11,22,123]
def weightSort(integers):
	res = sorted([str(x) for x in integers])
	res = sorted(res,key=lambda x: sum(int(d) for d in x))
	return res

print(weightSort(ls))
