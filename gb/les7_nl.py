nums = [1,3,6,-1,-3,-12,-5,5]
test = 'o'

def num0(x):
    res = []
    try:
        res = [j for j in x if j%3 == 0 and j > 0 and j%4!=0]
    except Exception as e1:
        print('Ошибка: ',e1)
    return res
print(num0(nums))
print(num0(test))
