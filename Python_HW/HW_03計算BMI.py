h = eval(input("請輸入身高(cm):"))
w = eval(input("請輸入體重(kg):"))
BMI = w/((h/100)**2)
print("您的BMI=","{:.2f}".format(BMI))
