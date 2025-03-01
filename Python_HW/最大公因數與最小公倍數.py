a,b=map(int,input().split())
# 計算最大公因數
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# 計算最小公倍數
def lcm(x, y):
    return x * y // gcd(x, y)

# 輸出結果
print("最大公因數:", gcd(a, b))
print("最小公倍數:", lcm(a, b))

for i in range(1,a+1):
    if a%i==0 and b%i==0:
        gcd=i
print(i)
print(a*b//gcd)