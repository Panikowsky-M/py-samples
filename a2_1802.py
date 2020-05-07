def longest(s,key=lambda x: x):
    max_st  = 0
    max_len = 0
    cur_len = 1
    cur_st  = 0

    for i in range(1,len(s)):
        if key(s[i-1]) <= key(s[i]):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                max_st = cur_st
            cur_st = i
            cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
        max_st  = cur_st

    return s[max_st:max_st+max_len]

print(longest('nab'))
