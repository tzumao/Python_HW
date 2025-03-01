def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
m=[]
num=2
while len(m)<6:
    if prime(2**num-1):
        m.append(2**num-1)
        print(2**num-1)
    num+=1