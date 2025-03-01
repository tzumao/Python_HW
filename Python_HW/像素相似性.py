a,b = map(int,input().split())
now1 = 2** (8-1)
now2 = 2** (8-1)
a1=[]
b1=[]
while now1>0:
    a1.append(a//now1)
    a %= now1
    now1 //= 2
while now2>0:
    b1.append(b//now2)
    b %= now2
    now2 //= 2
count=0
for i in range(7,0,-1):
    if a1[i]==b1[i]:
        count+=1
print(count)
