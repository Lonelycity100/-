import random
print('正在开奖中')
jiang=[]
while len(jiang)<3:
    num=random.randint(1,8)
    if num not in jiang:
        jiang.append(num)
print(jiang)