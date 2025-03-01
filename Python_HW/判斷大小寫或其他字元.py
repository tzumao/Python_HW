# 讀入字元
char = input("請輸入一個字元: ")

# 判斷字元類型
if char.isupper():
    print(f"{char} 是大寫字母。")
elif char.islower():
    print(f"{char} 是小寫字母。")
else:
    print(f"{char} 不是大寫或小寫字母。")
