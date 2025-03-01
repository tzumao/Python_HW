x=input().split()
print(len(x))
x=''.join(x)
def search(s,n):
    count=0
    for i in s:
        if i==n:
            count+=1
    return count
seen_letter=[]
for i in x:
    if i.isalpha() and i not in seen_letter:  # 確保只處理字母且不重複
        seen_letter.append(i)  # 添加到已出現的字母中
        print(i,"=",search(x,i))
