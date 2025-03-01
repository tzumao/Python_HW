# 輸入三個整數
a = int(input("請輸入係數 a: "))
b = int(input("請輸入係數 b: "))
c = int(input("請輸入常數項 c: "))

# 計算判別式
discriminant = b**2 - 4 * a * c

# 根據判別式判斷實數根的數量
if discriminant > 0:
    print("該方程式有兩個不同的實數根。")
elif discriminant == 0:
    print("該方程式有一個實數根。")
else:
    print("該方程式沒有實數根。")
