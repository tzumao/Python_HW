n = int(input())
drink = n
while n >=3 :
    drink += n // 3
    n = n % 3 + n // 3
print(drink)
