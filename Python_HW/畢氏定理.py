x=500**2
for i in range(1,501):
    for j in range(1,501):
        z=i**2+j**2
        if z<x:
            print(round(z**0.5,2),i,j)
            if i>j:
                print(i)
            else:
                print(j)
        else:
            break
            