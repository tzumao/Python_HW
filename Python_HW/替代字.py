# 輸入字串、要替換的字和新字
text = input("請輸入一段文字：")
old_char = input("請輸入要替換的字：")
new_char = input("請輸入新的字：")

# 使用 replace 方法替換字元
result = text.replace(old_char, new_char)

# 輸出結果
print("替換後的文字：", result)
