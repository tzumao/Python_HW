def f(n):
    if n<10:
        return 1
    else:
        return 1+f(n//10)
n=int(input())
print(f(n))