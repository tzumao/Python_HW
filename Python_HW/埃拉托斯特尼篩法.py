def sieve_of_eratosthenes(n):
    # 建立一個布林陣列，初始值全為 True，表示所有數都可能是質數
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是質數

    # 開始篩選質數
    #​n**0.5是篩選的最大範圍，因為超過這個範圍的數的倍數已經被處理過了。
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:  # 如果 i 是質數
            for j in range(i * i, n + 1, i):  # 將 i 的倍數標記為非質數
                is_prime[j] = False

    # 將所有是質數的數字收集到列表中
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes

# 測試
n = int(input("請輸入篩選範圍的上限 n："))
primes = sieve_of_eratosthenes(n)
print(f"小於等於 {n} 的質數有：")
print(primes)
