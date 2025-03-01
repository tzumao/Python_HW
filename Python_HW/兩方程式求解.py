# 使用者輸入六個整數
a = int(input("請輸入 a: "))
b = int(input("請輸入 b: "))
c = int(input("請輸入 c: "))
d = int(input("請輸入 d: "))
e = int(input("請輸入 e: "))
f = int(input("請輸入 f: "))

# 計算行列式
denominator = a * e - b * d

# 檢查行列式是否為零
if denominator == 0:
    print("此方程組無唯一解或無解。")
else:
    # 使用克拉默法則求解 x 和 y
    x = (c * e - b * f) / denominator
    y = (a * f - c * d) / denominator
    print(f"方程組的解為 x = {x}, y = {y}")