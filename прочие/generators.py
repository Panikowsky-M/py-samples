import random 

nums = [1,2,3,4,-1,-2,-3,4]
pairs = [(1,'a'),(2,'b'),(3,'c')]

res = filter(lambda x : x > 0, nums)
print("Вывод списка полученного лямбда-функцией:\n%s\n" % list(res))

res = [n for n in nums if n > 0]
print("Вывод списка полученного генератором:\n%s\n" % res)

res = {p[0]:p[1] for p in pairs}
print("Вывод словаря полученного генератором:\n%s\n" % res)


nums = [random.randint(1,100) for i in range(5)]
nums = [n**2 for n in nums]
print("Квадраты чисел полученные генератором:\n%s\n" % nums)

names = ['Андрей','Владимир','Сергей','Афанасий']

names = [j for j in names if j.startswith('А')]

print("Генератор имен начинающихся на А:\n%s\n" % names)
