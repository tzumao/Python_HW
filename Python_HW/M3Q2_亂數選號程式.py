import random
numbers = random.sample(range(1, 43), 6)
output = '\t'.join(map(str, numbers))
print(output)
#x=[random.randint(1,42)for i in range(6)]這個方法會選到重覆數字
#x=random.sample(range(1,42),6)這個不會選到重覆數字
