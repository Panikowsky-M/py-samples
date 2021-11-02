# Мемоизация для базовых случаев
memo = {0: 0, 1: 1}

def fib1(n):
    if n  not in memo:
        memo[n] = fib1(n - 1) + fib1(n - 2)
    return memo[n]

print(fib1(5))
print(fib1(15))
