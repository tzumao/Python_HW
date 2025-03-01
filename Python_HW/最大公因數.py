def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(x,x%y)