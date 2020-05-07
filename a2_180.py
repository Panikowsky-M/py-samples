def longest(n,*args):
    lst = [[n]]
    for s in args:
        if s > n: lst[-1].append(s)
        else:
            n = s
            lst.append([s])
    return ''.join(max(lst))

s = longest(*'abcdeapbcdef')
print(s)
