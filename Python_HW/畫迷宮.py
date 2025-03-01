x=input()
n=0
for i in x:
    if i=='b':
        print(' '*n,end='')
        n=0
    elif i=='!':
        print()
        n=0
    elif '0'<=i<='9':
        n+=int(i)
    else:
        print(i*n,end="")
        n=0