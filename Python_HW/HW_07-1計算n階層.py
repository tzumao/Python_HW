n = eval(input("請輸入n值,我幫你算n階乘:"))
x=1
y=1
if n>0:
    while x<=n:
        y*=x
        x+=1
    else:
        print(n,"!=",y)
elif n==0:
    print("0! = 1")
else:
    print("不合法的輸入值,n應該大於等於0!")
