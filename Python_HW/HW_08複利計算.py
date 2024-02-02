x = eval(input("請輸入您的本金:"))
rate = (eval(input("請輸入您的年利率(如1.23=1.23%):")))/100
year = eval(input("請輸入期數(年):"))
for i in range(1,year+1,1):
    y=x*(1+rate)**i
    print("您第 {} 年的本利和為: {:.2f}".format(i,y))
