def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(2,(n+1)//2):
    if prime(i) and prime(n-i):
        print("%d+%d"%(i,n-i))