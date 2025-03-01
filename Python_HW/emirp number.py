def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=[]
n=3
while len(x)<10:
    digit_sum=sum(list(map(int,str(n))))
    if prime(n) and prime(digit_sum):
        x.append(n)
        print(n)
    n+=1