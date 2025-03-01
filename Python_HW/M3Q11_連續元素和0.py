n=int(input())
num=list(map(int,input().split()))
for i in range(n):
    tmp=0
    for j in range(i,n):
        tmp+=num[j]
        if(tmp==0):
            for k in range(i,j+1):
                print(num[k],end=" ")
            print()