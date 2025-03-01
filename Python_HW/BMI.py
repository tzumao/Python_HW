a,b=map(int,input().split())
BMI=b/(a/100)/(a/100)
if BMI<18.5:
    print("體重過輕")
elif BMI<24:
    print("正常範圍")
elif BMI<27:
    print("過重")
elif BMI<30:
    print("輕度肥胖")
elif BMI<35:
    print("中度肥胖")
else:
    print("重度肥胖")