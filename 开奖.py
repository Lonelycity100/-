import random
print('正在开奖中')
red=[]
blue=0
while len(red)<5:
    num=random.randint(1,20)
    if num not in red:
        red.append(num)
red.sort()
print(red)
blue=random.randint(1,8)
print(blue)