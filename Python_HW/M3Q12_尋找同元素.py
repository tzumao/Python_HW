m,n=map(int,input().split())
f=list(set(map(int,input().split())))
g=list(set(map(int,input().split())))
count=0
for i in range(len(f)):
    for j in range(len(g)):
        if f[i]==g[j]:
            count+=1
            break
print(count)