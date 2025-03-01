n=int(input())
sum=0
for i in range(2,n+1):
    num=i
    while num>1:
        if num%2==0:
            num//=2
        elif num%3==0:
            num//=3
        elif num%5==0:
            num//=5
        else:
            break
    if num==1:
        sum+=i
print(sum)