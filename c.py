Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ls = [9, 21, 32, 55, 81, 11]
>>> ls.sort(key = lambda x: sum(int (i) for i in str(x)),reverse = True)
>>> ls
[55, 9, 81, 32, 21, 11]
>>> ls = [56, 65, 74, 100, 99, 68, 86, 180, 90]
>>> ls.sort(key = lambda x: sum(int (i) for i in str(x)),reverse = True)
>>> ls
[99, 68, 86, 56, 65, 74, 180, 90, 100]
>>> ls = [56, 65, 74, 100, 99, 68, 86, 180, 90]
>>> ls.sort(key = lambda x: sum(int (i) for i in str(x)),reverse = True)
>>> ls
[99, 68, 86, 56, 65, 74, 180, 90, 100]
>>> ls = [103, 123, 4444, 99, 2000]
>>> ls.sort(key = lambda x: sum(int (i) for i in str(x)),reverse = True)
>>> ls
[99, 4444, 123, 103, 2000]
>>> ls.sort(key = lambda x: sum(int (i) for i in str(x)))
>>> ls
[2000, 103, 123, 4444, 99]
>>> 