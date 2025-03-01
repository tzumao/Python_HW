def e(n):
    y=1
    sum=1
    for i in range(1,11):
        y*=i
        sum+=round((n**i/y),2)
    return sum
print(e(1))