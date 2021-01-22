from django.db import connection
from websend import models
#检查用户登录是否成功
def checkLogin(username,password):
    finduser=models.User.objects.filter(username=username).first()
    print(finduser.pk)
    print(finduser.password)
    if password==finduser.password and finduser.role.pk==3:
        return  finduser.pk
    else:
        return -1
#根据用户id获取购票人信息
def getFaninfo(id):
    user=models.User.objects.get(pk=id)
    faninfo=models.Fan.objects.filter(user=user).first()
    print(user.username)
    print(faninfo.gender)
    print(faninfo.is_select)
    print(faninfo.account)
    return user.username,faninfo
#充值
def chongMoney(userid,password,money):
    user=models.User.objects.get(pk=userid)
    psd=user.password
    if(psd!=password):
        return 0
    else:
        oldmoney=models.Fan.objects.filter(user=user).first().account
        faninfo = models.Fan.objects.filter(user=user).update(account=oldmoney+int(money))
        return 1
#根据用户名获取其票信息
def getTicketByuser(username):
    user=models.User.objects.filter(username=username).first()
    fan=models.Fan.objects.filter(user=user).first()
    tk_users=models.FanTicket.objects.filter(fan=fan)
    return tk_users

#显示演唱会列表信息
def allConcert():
    concerts=models.Concert.objects.all()
    res=[]
    for concert in concerts:
        res.append(concert)
    return res
#根据id查找演唱会
def findConcert(id):
    concert=models.Concert.objects.get(pk=id)
    return concert
#根据name查找演唱会
def findConcertByname(name):
    concert=models.Concert.objects.filter(name=name).first()
    return concert
#显示当前演唱会的各种票的余量
def findTicket(id):
    concert=models.Concert.objects.get(pk=id)
    tickets=models.Ticket.objects.filter(concert=concert)
    for ticket in tickets:
        if int(ticket.type)==0:
            vipt=ticket
        if int(ticket.type)==1:
            innt=ticket
        if int(ticket.type) == 2:
            outt=ticket
    return vipt,innt,outt
#获取某个演唱会某种类型的票价
def findTkPrice(concertname,tkname):
    concert=models.Concert.objects.filter(name=concertname).first()
    tk=models.Ticket.objects.filter(concert=concert,name=tkname).first()
    return tk.price
#根据演唱会名称及票的类型获取票
def findTk(concertname,tkname):
    concert = models.Concert.objects.filter(name=concertname).first()
    tk = models.Ticket.objects.filter(concert=concert, name=tkname).first()
    return tk
#判断
def judge(stu_name,stu_num,gender,tk_name,concertname,count):
    # 检查所选票类型是否一致
    buflag = True
    tmp = tk_name[0]
    for each in tk_name:
        if each != tmp:
            buflag = False
    if (buflag != True):
        return "购票人所购买票类型不一致"
    all_tk = tk_name[0]
    price=findTkPrice(concertname,all_tk)
    # 检查各学生是否都处于可选状态
    user_ids = []
    for i in range(1, len(stu_num) + 1):
        each_stu_num = stu_num[i - 1]
        each_stu_name = stu_name[i - 1]
        each_gender=gender[i-1]
        stu = models.Fan.objects.filter(cardid=each_stu_num).first()
        if stu==None:
            return "购票人" + str(i) + "填写信息有误"
        user_ids.append(stu.user.pk)
        if stu.name != each_stu_name or int(stu.gender) != int(each_gender):
            return "购票人" + str(i) + "填写信息有误"
        if int(stu.is_select) == 1:
            return "购票人" + str(i) + "处于不可选宿舍状态"
        if int(stu.account)<price:
            return "购票人" + str(i) + "账户余额不足"

    #检查余票是否充足
    concert = models.Concert.objects.filter(name=concertname).first()
    tk = models.Ticket.objects.filter(concert=concert, name=all_tk).first()
    if(int(tk.remain)<int(count)):
        return "余票不足，请刷新重试"

    return "准备就绪"