# 使用者輸入金額和購買數量
n = int(input("媽媽給了多少錢："))
a = int(input("蘋果的數量："))
b = int(input("柳丁的數量："))
c = int(input("桃子的數量："))

# 單價
price_apple = 15
price_orange = 20
price_peach = 30

# 計算購物總金額
total_cost = a * price_apple + b * price_orange + c * price_peach

# 計算找零金額
change = n - total_cost

# 計算最少銅板數
fifty_count = change // 50  # 50元的銅板數
change %= 50  # 更新找零金額

five_count = change // 5    # 5元的銅板數
change %= 5   # 更新找零金額

one_count = change          # 剩下的全用1元銅板

# 輸出結果
print("老闆需找的銅板數：")
print(f"50元：{fifty_count} 個")
print(f"5元：{five_count} 個")
print(f"1元：{one_count} 個")
