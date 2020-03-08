c = 0
arr = [-3,5,8,-9,4,-6]
ne = -1
for j in range(len(arr)):
	if arr[j] < 0:
		ne = j
		c+=arr[j]
		break
for j in range(ne+1,len(arr)):
	print(arr[j])
	c+=arr[j]
print(c)
