n=int(input())
num=list(map(int,input().split()))
maxV=float('-inf')
for i in range(n):
    tmp=1
    for j in range(i+1,n):
        tmp*=num[j]
        if(tmp>maxV):
            maxV=tmp
print(maxV)