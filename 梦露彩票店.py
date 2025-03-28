import random
def pd(r,b,n):
    global rq,blue,blues
    if redcount==r:
        if bool(blues==blue)==b:
            rq=n
count=int(input('欢迎使用梦露彩票店智能投注系统，您正在购买双色球第五期，请问要投多少注？:'))
ji=input('机选or自选:')
bei=int(input('倍率:'))
reds=[4, 9, 13, 17, 19]
blues=7
all=0

print('中奖号码是:红球',reds,'蓝球',blues)
for i in range(1,count+1):
    jiang=0
    rq=0
    red,blue,rqs=[],0,[]
    redcount=0
    while len(red)<5:
        num=random.randint(1,20)
        if num not in red:
            red.append(num)
    red.sort()
    blue=random.randint(1,8)
    for j in reds:
        if j in red:
            redcount+=1
    pd(0,0,1)
    pd(1,0,3)
    pd(2,0,3)
    pd(3,0,5)
    pd(4,0,10)
    pd(5,0,150)
    pd(0,1,3)
    pd(1,1,5)
    pd(2,1,10)
    pd(3,1,50)
    pd(4,1,100)
    pd(5,1,1000)
    print('第',i,'注是:红球',red,'蓝球',blue,'共中',rq*bei,'rq')
    all+=rq*bei
print(all)