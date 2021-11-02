def fib1(n):
    if n == 0: return n
    last = 0
    next = 1
    for _ in range(1,n):
    # Распаковка кортежа
        last, next = next, last + next
    return next

print(fib1(5))
print(fib1(15))
