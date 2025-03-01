def leading_digit(num1, num2):
    x=int(num1[0])
    y=int(num2[0])
    if x>y:
        return num1
    else:
        return num2
num1,num2=input().split()
print(leading_digit(num1, num2))