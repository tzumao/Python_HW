n = int(input())
now = 2** (8-1)
while now>0:
    print(n//now,end="")
    n %= now
    now //= 2