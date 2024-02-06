suits=("梅花","方塊","紅心","黑桃")
ranks=("A","2","3","4","5","6","7","8","9","10","J","Q","K")

pokers=[(i,j)for i in suits for j in ranks]
import random
random.shuffle(pokers)

players=[[],[],[],[]]

while len(pokers)!=0:
    for i in range(4):
        players[i].append(pokers.pop())

for i in range(4):
    print(f"player{i}=",end="")
    for card in players[i]:
            print("".join(card),end=",")
    print()
