n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i+j+k<=n:
                if i<j and j<k and i**2+j**2==k**2:
                    print("%d\t%d\t%d"%(i,j,k))