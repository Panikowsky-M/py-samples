def fib1(n):
    yield 0
    if n > 0: yield 1
    last = 0
    next = 1
    for _ in range(1,n):
        last, next = next, last + next
        yield next

for i in fib1(15):
    print(i)
