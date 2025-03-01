n=int(input())
count=0
while n>0:
    num=n%10
    if num==7:
        count+=1
    n//=10
print(count)


