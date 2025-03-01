n=int(input())
sum=0
count=0
while n>0:
    sum+=n%10
    n//=10
    count+=1
print(count)
print(sum)

#sum2 = sum(map(int, str(n)))


