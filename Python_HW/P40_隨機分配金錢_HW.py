import random
money=10000
p=[0]*5
for i in range(4):
    p[i]=random.randint(0,money)
    money-=p[i]
p[4]=money
print(p)