start1,start2=map(int,input().split())
end1,end2=map(int,input().split())
start_time = start1 * 60 + start2
end_time = end1 * 60 + end2

# 總停車時間（分鐘）
total_minutes = end_time - start_time

# 計算費用
cost = 0

# 前2小時（120分鐘內）的費用
if total_minutes <= 120:
    cost += (total_minutes // 30) * 30
else:
    cost += (120 // 30) * 30
    total_minutes -= 120

    # 2到4小時（120到240分鐘內）的費用
    if total_minutes <= 120:
        cost += (total_minutes // 30) * 40
    else:
        cost += (120 // 30) * 40
        total_minutes -= 120

        # 超過4小時的費用
        cost += (total_minutes // 30) * 60

# 輸出結果
print(cost)
