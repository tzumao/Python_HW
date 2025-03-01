# 讀入年份
year = int(input("請輸入一個4位數的整數年份: "))

# 判斷閏年
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是閏年。")
else:
    print(f"{year} 不是閏年。")
