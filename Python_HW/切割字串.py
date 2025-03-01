# 輸入文字和切割符號
text = input("請輸入一段文字：")
delimiter = input("請輸入切割符號：")

# 使用指定符號切割文字
substrings = text.split(delimiter)

# 列印每個子字串
for substring in substrings:
    print(substring)
