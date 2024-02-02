import random
count=0
while True:
    block1=random.randint(0,1)
    block2=random.randint(0,1)
    count+=1
    if block1==block2:
        print("笑筊({},{})".format(block1,block2))
    else:
        print("聖筊({},{})".format(block1,block2))
        break
print("您擲了{}次才擲到聖筊".format(count))
