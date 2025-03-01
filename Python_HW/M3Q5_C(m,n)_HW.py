def f(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum
m,n=map(int,input().split())
print(f(m)//(f(n)*f(m-n)))