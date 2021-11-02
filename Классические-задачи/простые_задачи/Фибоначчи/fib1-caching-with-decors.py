from functools import lru_cache

@lru_cache(maxsize=None)
def fib1(n):
    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)

print(fib1(5))
print(fib1(15))
