def power1(a,n):
    if n==0:
        return 1
    else:
        return a*power1(a,n-1)
def power2(a,n):
    if n==0:
        return 1
    elif n%2==0:
         return power2(a,n//2)*power2(a,n//2)
    else:
        return a*power2(a,n-1)
a,b=map(int,input().split())
print(power1(a,b))
print(power2(a,b))