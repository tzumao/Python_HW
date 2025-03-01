N=int(input())
count=True
for i in range(1,N):
    s=str(i)
    sum=i
    for j in range(i+1,N):
        s=s+"+"+str(j)
        sum+=j
        if sum==N:
            count=False
            print(s)
            break
if count:
    print("No")