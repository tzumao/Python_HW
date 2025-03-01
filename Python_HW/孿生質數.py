def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
twin_prime=[]
num=3
while len(twin_prime)<6:
    if prime(num) and prime(num+2):
        twin_prime.append([num,num+2])
        print(num,num+2)
    num+=1