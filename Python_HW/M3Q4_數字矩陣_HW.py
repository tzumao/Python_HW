def F(w,h):
    for i in range(1,h+1):
        for j in range(2,w+1):
            print(i*j,end="\t")
        print()
F(5,3)