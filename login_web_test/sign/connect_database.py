from django.db import connection
from sign import models

#根据用户名查找用户
def find(user):
    user_info=models.User.objects.filter(username=user)
    for true_user in user_info:
        return true_user
#根据关键字查找用户
def findUsersp(keyword):
    print(keyword)
    users = models.User.objects.all()
    res = []
    for user in users:
        strname = str(user.username)
        if keyword in strname :
            res.append(user)
    return res
#添加用户
def addUser(username,password,rolename):
    try:
        role_obj=models.Role.objects.filter(rolename=rolename).first()
        newuser = models.User(username=username, password=password, role=role_obj)
        newuser.save()
        return True
    except Exception as e:
        return False
#修改用户
def modifyUser(username,newpass,newrolename):
    try:
        newrole=models.Role.objects.filter(rolename=newrolename).first()
        res=models.User.objects.filter(username=username).update(password=newpass,role=newrole)
        return True
    except Exception as e:
        return False
#删除用户
def delUser(id):
    flag=True
    try:
        user=models.User.objects.get(pk=id)
        print(user.pk)
        rolename=user.role.rolename
        print(rolename)
        if rolename == '歌手':
            singers=models.Singer.objects.all()
            for singer in singers:
                if singer.user.pk==user.pk:
                    concerts=models.Concert.objects.all()
                    for concert in concerts:
                        if concert.singer.pk==singer.pk:
                            tickets=models.Ticket.objects.all()
                            for tk in  tickets:
                                if tk.concert.pk==concert.pk:
                                    fts=models.FanTicket.objects.all()
                                    for ft in  fts:
                                        if ft.ticket.pk==tk.pk:
                                            res1=models.FanTicket.objects.filter(ticket=tk).delete()
                                            break
                                    res2=models.Ticket.objects.filter(concert=concert).delete()
                                    break
                            res3=models.Concert.objects.filter(singer=singer).delete()
                            break
                    res4=models.Singer.objects.filter(user=user).delete()
                    break
        else:
            print("111")
            fans=models.Fan.objects.all()
            for fan in fans:
                print(fan.user.pk)
                if fan.user.pk==user.pk:
                    print("222")
                    fts=models.FanTicket.objects.all()
                    for ft in fts:
                        if ft.fan.pk==fan.pk:
                            res5=models.FanTicket.objects.filter(fan=fan).delete()
                            break
                    res6=models.Fan.objects.filter(user=user).delete()
                    break
        res4=models.User.objects.get(pk=id).delete()
        flag=True
    except Exception as e:
        flag=False
    return flag
#根据id查找用户
def findUserpk(id):
    user=models.User.objects.get(pk=id)
    return user
#修改用户密码
def moPass(user,newpass):
    flag=True
    try:
        newuser=models.User.objects.filter(username=user).update(password=newpass)
        print(newuser)
        flag=True
    except Exception as e:
        flag=False
    return  flag

#欢迎页面统计
def findAll():

    concertnum=0
    managernum=0
    singernum=0
    fannum=0
    concerts=models.Concert.objects.all()
    concertnum=len(concerts)
    managers=models.User.objects.filter(role=1)
    managernum=len(managers)
    singers=models.User.objects.filter(role=2)
    singernum=len(singers)
    fans=models.User.objects.filter(role=3)
    fannum=len(fans)

    return concertnum,managernum,singernum,fannum


#插入新用户
def insert(user,password,role):
    cursor=connection.cursor()
    b=False
    try:
        #插入
        #for i in range(100000):
        cursor.execute("insert into users(username,password,role_id) values ('"+user+"', '"+password+"', '"+role+"')")
        b=True
    except:
        b=False
    return b
#查询用户角色
def search_role(role_id):
    role_info=models.Role.objects.get(pk=role_id)
    return role_info
#查询所有用户
def findUserAll():
    users = models.User.objects.all()
    res = []
    for user in users:
        res.append(user)
    return res
#查询当前角色权限
def add_nodes(role_id,node_names):
    cursor=connection.cursor()
    #通过role_id查询其对应的node_id
    cursor.execute("select * from role_node where role_id='" + str(role_id) + "'")
    rows=cursor.fetchall()
    for row in rows:
        node_id=row[2]
        cursor.execute("select * from node where id='" + str(node_id) + "'")
        newrow=cursor.fetchone()
        node_names.append(str(newrow[1]))
#显示演唱会
def findConcertAll():
    concerts=models.Concert.objects.all()
    ct=[]
    for c in concerts:
        ct.append(c)
    return ct
#显示演唱会门票
def findTkConcertAll():
    tickets=models.Ticket.objects.all()
    tk=[]
    for ticket in  tickets:
        tk.append(ticket)
    return tk