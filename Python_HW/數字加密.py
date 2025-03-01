num=input()
x=[]
for i in num:
    x.append((int(i)+7)%10)
a=x[0]
b=x[1]
c=x[2]
d=x[3]
a,c=c,a
b,d=d,b
print(''.join((str(a),str(b),str(c),str(d))))