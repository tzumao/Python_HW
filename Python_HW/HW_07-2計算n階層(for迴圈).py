n = eval(input("請輸入n值,我幫你算n階乘:"))
ans = 1
if n>0:
    for i in range(1,n+1,1):
        ans*=i  
    print("{}!={}".format(n,ans))
elif n==0:
    print("0! = 1")
else:
    print("不合法的輸入值,n應該大於等於0!")
