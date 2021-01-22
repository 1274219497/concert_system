from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from websend import database_handle as dh
from websend.rabbitSend import RabbitMQSend as RS
from websend import jwt_tool
# Create your views here.

def first(request):
    return render(request,"login.html")
#判断是否能登录，能登录将token返给前端
def loginController(request):
    username=request.POST.get("user")
    psd=request.POST.get("password")
    userid = dh.checkLogin(username, psd)
    # 模拟登录
    if(userid!=-1) :

        # 用户标识id
        info = {"user_id": userid}
        # 生成token
        token = jwt_tool.gen_token(info)
        # 返回数据
        data = {"msg": "登录成功!", "token": token, "code": 1}

        return render(request,"midlink.html",data)
    else:
        messages.success(request, "用户名或密码错误或用户无登录权限，请重新输入")
        return redirect('/login/')

#获取当前用户信息
def getdata(request,token):

        # 解析token获取用户身份信息
    res = jwt_tool.parser_token(token)
    if res["code"] == 1:
        user_id = res["data"]["user_id"]
        username,faninfo=dh.getFaninfo(user_id)
        print(token)
        return  render(request,"faninfo.html",{"username" :username,"gender":int(faninfo.gender),
                                               "is_select":int(faninfo.is_select),
                                               "account":faninfo.account,"token":token})
    else:
        return JsonResponse({"msg": "身份验证失败 请重新登录!"}, safe=False)
#用户主页信息
def faninfo(request):
    token=request.GET.get("token")
    # 解析token获取用户身份信息
    res = jwt_tool.parser_token(token)
    if res["code"] == 1:
        user_id = res["data"]["user_id"]
        username, faninfo = dh.getFaninfo(user_id)
        return render(request, "faninfo.html",
                        {"username": username, "gender": int(faninfo.gender), "is_select": int(faninfo.is_select),
                         "account": faninfo.account, "token": token})
    else:
        return JsonResponse({"msg": "身份验证失败 请重新登录!"}, safe=False)

#充值界面
def addMoneyIndex(request,token):

    print(token)
    return render(request,"addMoneyIndex.html",{"token":token})
def addMoneyIndexOther(request):
    token=request.GET.get("token")
    print(token)
    return render(request, "addMoneyIndex.html", {"token": token})

#充值操作
def addMoney(request,token):
    money=request.POST.get("money")
    password=request.POST.get("pass")
    repassword=request.POST.get("repass")
    print(money)
    print(password)
    print(repassword)
    if(password!=repassword):
        messages.success(request, "两次密码不一致或者密码输入错误")
        redirect('/addMoneyIndexOther/?token='+token)
    res = jwt_tool.parser_token(token)
    if res["code"] == 1:
        user_id = res["data"]["user_id"]
        print(user_id)
        if(dh.chongMoney(user_id,password,money)==1):
            messages.success(request, "充值成功")
            return redirect('/faninfo/?token=' + token)
    messages.success(request, "两次密码不一致或者密码输入错误")
    return redirect('/addMoneyIndexOther/?token=' + token)
#开始购票界面
def start(request):
    concerts=dh.allConcert()
    count=[]
    for i in  range(1,len(concerts)+1):
        count.append(i)

    return render(request,"start.html",{"concerts":concerts,"count":count})
#查看已购票界面
def search(request,username):
    tk_users=dh.getTicketByuser(username)
    tks=[]
    for tk_user in tk_users:
        tks.append(tk_user.ticket)
    return render(request,"showTK.html",{"tks":tks,"len":len(tks)})

#进入购票页面
def selectDorindex(request):
    id=request.POST.get("concert")
    if id==None:
        messages.success(request, "未选择演唱会")
        return redirect('/start/')
    remain_seat=request.POST.get("remain_seat"+str(id))
    if int(remain_seat)== 0:
        messages.success(request, "该场演唱会暂无余票")
        return redirect('/start/')
    vipt,innt,outt=dh.findTicket(id)
    concert=dh.findConcert(id)
    return render(request,"selectDor.html",{"concert":str(concert.name),"vipt":int(vipt.remain),"innt":int(innt.remain),"outt":int(outt.remain)})

#购票人数处理
def selectDorFirst(request):
    count=request.GET.get("count")
    concertname = request.GET.get("conname")
    #检查同住人数量是否符合规范
   # print(count)
    url='/selectSecond/?count='+count+'&conname='+concertname
    return HttpResponse(url)

def selectDorSecond(request):
    count=request.GET.get("count")
    concertname=request.GET.get("conname")
    print(count)
    print(concertname)
    concert=dh.findConcertByname(concertname)
    countnum = []

    for i in range(1, int(count) + 1):
        countnum.append(i)

    ticketnames = []
    vipt,innt,outt=dh.findTicket(concert.pk)
    tickets=[]
    tickets.append(vipt)
    tickets.append(innt)
    tickets.append(outt)
    for ticket in tickets:
        if(int(ticket.remain)>=int(count)):
            ticketnames.append(ticket.name)

        #print(bu.name)
    info = {'count': countnum, 'countlen': count, 'tickets': ticketnames,'concertname':concertname}
    return render(request, "selectForm.html", info)


#购票逻辑
def selectDorAction(request,count,concertname):
    stu_name = []
    stu_num = []
    gender = []
    tk_name = []
    for i in range(int(count)):
        temp_stuname = request.GET.get("stuname" + str(i + 1))
        if temp_stuname != None:
            stu_name.append(temp_stuname)
        temp_stunum = request.GET.get("stunum" + str(i + 1))
        if temp_stunum != None:
            stu_num.append(temp_stunum)
        temp_gender = request.GET.get("gender" + str(i + 1))
        if temp_gender != None:
            gender.append(temp_gender)
        temp_buname = request.GET.get("tkname" )
        if temp_buname != None:
            tk_name.append(temp_buname)
    tmpstr=dh.judge(stu_name,stu_num,gender,tk_name,concertname,count)
    if(tmpstr!="准备就绪"):
        messages.success(request,tmpstr)
        return redirect('/selectSecond/?count='+count+'&conname='+concertname)
    else:
        body=""
        body=body+str(count)+" "
        for num in stu_num:
            body=body+str(num)+" "
        all_gender=gender[0]
        all_tk=tk_name[0]
        concert=dh.findConcertByname(concertname)
        tk=dh.findTk(concertname,all_tk)
        print(tk.pk)
        print(concert.pk)
        body=body+str(all_gender)+" "+str(tk.pk)+" "+str(concert.pk)
        RS(body)#向rabbitMQ消息队列发送消息#暂时先注释
        messages.success(request, "购票成功")
        return redirect('/login/')

