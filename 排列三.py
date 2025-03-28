import random
count=int(input('欢迎使用梦露彩票店智能投注系统，您正在购买排列三第一期，请问要投多少注？:'))
ji=input('机选or自选:')
rqs=0
bei=int(input('倍率:'))
jiang=[3, 7, 8]
for i in range(1,count+1):
    piao,rq,ok=[],1,0
    while len(piao)<3:
        num=random.randint(1,8)
        if num not in piao:
            piao.append(num)
    for j in range(3):
        if jiang[j]==piao[j]:
            ok+=1
    if ok==1:
        rq=3
    if ok==2:
        rq=10
    if ok==3:
        rq=100
    print('第',i,'注是:',piao,'共中',rq*bei,'rq')
    rqs+=rq*bei
print(rqs)