from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from sign.class_col import usr
from sign import connect_database as cd
import json
# Create your views here.
def analysis_str_list(s):
    """自定义解析列表的方法"""
    print(s)
    this_list = []
    print(s)
    li = s.replace("[", "").replace("]", "").split(",")
    print(li)
    for i in li:
        tmp=[]
        temp=""
        for j in i:
            try:
                int(j)
                tmp.append(j)
            except Exception as e:
                pass
        if len(tmp)!=0:
            for num in tmp:
                temp+=str(num)
        newnum=int(temp)
        this_list.append(newnum)

    return this_list
users={}
#登录页面
def login(request):
    return render(request, "login.html")
#退出页面
def ret(request):
    username=request.GET.get("get")
    if username in users:
        del users[username]
    messages.success(request,"退出成功")
    return redirect("/login/")
#统计页面
def show(request):
    user_name = request.GET.get("username")
    role = request.GET.get("role")
    conlist=cd.findConcertAll()
    tklist=cd.findTkConcertAll()
    info = {'username': user_name, 'role': role,'conlist':conlist,'tklist':tklist}

    # 在此处获取权限，判断是否有该权限
    return render(request, "show_tongji.html", info)
#统计页面
def show_singer(request):
    user_name = request.GET.get("username")
    role = request.GET.get("role")
    conlist=cd.findConcertAll()
    tklist=cd.findTkConcertAll()
    info = {'username': user_name, 'role': role,'conlist':conlist,'tklist':tklist}

    # 在此处获取权限，判断是否有该权限
    return render(request, "show_tongji_singer.html", info)

#用户管理
class UserController:
    # 歌手欢迎页面
    def managerWelcome(request):
        user_name = request.GET.get("username")
        role = request.GET.get("role")
        total_list = cd.findAll()
        info = {'username': user_name, 'role': role, 'cn': total_list[0],
                'tn': total_list[1], 'mn': total_list[2], 'sn': total_list[3]}

        return render(request, "index_manager.html", info)

    #后台管理者欢迎页面
    def teacherWelcome(request):
        user_name = request.GET.get("username")
        role = request.GET.get("role")
        total_list = cd.findAll()
        info = {'username': user_name, 'role': role ,'cn':total_list[0],
                'tn':total_list[1], 'mn':total_list[2], 'sn':total_list[3]}

        return render(request, "index_teacher.html", info)

    #用户登录处理逻辑
    def userLogin(request):
        if request.method == 'POST':
            if 'login' in request.POST:
                user=request.POST.get("user")
                password=request.POST.get("password")
                print("user:"+user)
                user_info=cd.find(user)
                if(user_info!=None):
                    right_password=user_info.password
                    if(password==right_password):
                        node_names=[]
                        rolename=cd.search_role(user_info.role.id).rolename
                        cd.add_nodes(user_info.role,node_names)
                        print(node_names)
                        true_user=usr(user,rolename)
                        true_user.node_names=node_names
                        print(true_user.node_names)
                        users[user]=true_user
                        total_list = cd.findAll()
                        info = {'username': user, 'role': rolename, 'cn': total_list[0],
                                'tn': total_list[1], 'mn': total_list[2], 'sn': total_list[3]}
                        if true_user.role=='后台管理者':
                            return render(request, "index_teacher.html", info)
                        if true_user.role=='歌手':
                            return render(request, "index_manager.html",info)
                        else:
                            messages.success(request, "用户名或密码错误或用户无登录权限，请重新输入")
                            return redirect('/login/')
                    else:
                        messages.success(request, "用户名或密码错误或用户无登录权限，请重新输入")
                        return redirect('/login/')
                else:
                    messages.success(request, "用户名或密码错误或用户无登录权限，请重新输入")
                    return redirect('/login/')
    #修改密码页面
    def modifyPasswordview(request):
        user_name=request.GET.get("username")
        print(user_name)
        return render(request,"modifypassword.html",{'username':user_name})
    #修改密码处理逻辑
    def modifyPassword(request,username):
        user_name=username
        role = cd.find(user_name).role.rolename
        old_password = cd.find(user_name).password
        input_old_password=request.POST.get("oldpass")
        input_new_password=request.POST.get("newpass")
        re_new_password=request.POST.get("repass")
        print(old_password)
        print(input_old_password)
        print(input_new_password)
        print(re_new_password)
        if(old_password!=input_old_password):
            messages.success(request,"密码不正确或新密码不符合规范或两次密码输入不一致")
            return render(request,"modifypassword.html",{'username':user_name})
        if(len(input_new_password)<6 or len(input_new_password)>16):
            messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
            return render(request, "modifypassword.html", {'username': user_name})
        if(input_new_password!=re_new_password):
            messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
            return render(request, "modifypassword.html", {'username': user_name})
        else:
            if(cd.moPass(user_name,input_new_password)):
                messages.success(request,"修改成功")
                return redirect('/index_teacher/?username='+user_name+'&role='+role)
            else:
                messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
                return render(request, "modifypassword.html", {'username': user_name})
        # 修改密码处理逻辑
        # 修改密码页面
    def modifyPasswordview_singer(request):
        user_name = request.GET.get("username")
        print(user_name)
        return render(request, "modifypassword_singer.html", {'username': user_name})
    def modifyPassword_singer(request, username):
        user_name = username
        role = cd.find(user_name).role.rolename
        old_password = cd.find(user_name).password
        input_old_password = request.POST.get("oldpass")
        input_new_password = request.POST.get("newpass")
        re_new_password = request.POST.get("repass")
        print(old_password)
        print(input_old_password)
        print(input_new_password)
        print(re_new_password)
        if (old_password != input_old_password):
            messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
            return render(request, "modifypassword_singer.html", {'username': user_name})
        if (len(input_new_password) < 6 or len(input_new_password) > 16):
            messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
            return render(request, "modifypassword_singer.html", {'username': user_name})
        if (input_new_password != re_new_password):
            messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
            return render(request, "modifypassword_singer.html", {'username': user_name})
        else:
            if (cd.moPass(user_name, input_new_password)):
                messages.success(request, "修改成功")
                return redirect('/index_manager/?username=' + user_name + '&role=' + role)
            else:
                messages.success(request, "密码不正确或新密码不符合规范或两次密码输入不一致")
                return render(request, "modifypassword_singer.html", {'username': user_name})
    #查询用户页面
    def userList(request):
        user_name = request.GET.get("username")
        role = request.GET.get("role")

        userlist = cd.findUserAll()
        # 在此处获取权限，判断是否有该权限
        info = {'username': user_name, 'role': role, 'userlist': userlist}
        return render(request, "userlist.html", info)
    #查询用户处理逻辑
    def userSearch1(request,username,role):
        username=username
        role=role
        keyword=request.POST.get("keyword")
        userlist=cd.findUsersp(keyword)
        # 在此处获取权限，判断是否有该权限
        info = {'username': username, 'role': role, 'userlist': userlist}
        if keyword=="" or len(userlist)==0:
            messages.success(request,"关键词不能为空或未查到相关用户信息")
        return render(request, "userlist.html", info)
    #编辑用户页面
    def userEdit(request):
        userid=request.GET.get("userid")
        user=cd.findUserpk(userid)
        info={'userinfo':user}
        return render(request,"useredit.html",info)
    #编辑用户处理逻辑
    def userEditaction(request,username):
        newpass=request.POST.get("password")
        newroletext=request.POST.get("roletext")
        if newroletext=='0':
            newrolename="歌手"
        else :
            newrolename="购票人"

        print(username)
        print(newpass)
        print(newrolename)
        if(cd.modifyUser(username,newpass,newrolename)):
            messages.success(request,"修改成功")
        else:
            messages.success(request,"修改失败，请检查用户信息是否符合规范")
        user=cd.find(username)
        info={'userinfo':user}
        return render(request,"useredit.html",info)
    #删除用户页面
    def userDel(request):
        user_name = request.GET.get("username")
        role = request.GET.get("role")
        userlist = cd.findUserAll()
        # 在此处获取权限，判断是否有该权限
        info = {'username': user_name, 'role': role, 'userlist': userlist,'datalen': len(userlist)}
        return render(request, "userdel.html", info)
    #删除用户页面的查询
    def userSearch3(request, username, role):
        username = username
        role = role
        keyword = request.POST.get("keyword")
        userlist = cd.findUsersp(keyword)
        # 在此处获取权限，判断是否有该权限
        info = {'username': username, 'role': role, 'userlist': userlist,'datalen': len(userlist)}
        if keyword == "" or len(userlist) == 0:
            messages.success(request, "关键词不能为空或未查到相关用户信息")
        return render(request, "userdel.html", info)

    #添加用户页面
    def userAdd(request):
        user_name = request.GET.get("username")
        role = request.GET.get("role")
        userlist = cd.findUserAll()
        # 在此处获取权限，判断是否有该权限
        info = {'username': user_name, 'role': role, 'userlist': userlist,'datalen': len(userlist)}
        return render(request, "useradd.html", info)
    #添加用户页面的查询
    def userSearch2(request, username, role):
        username = username
        role = role
        keyword = request.POST.get("keyword")
        userlist = cd.findUsersp(keyword)
        # 在此处获取权限，判断是否有该权限
        info = {'username': username, 'role': role, 'userlist': userlist,'datalen': len(userlist)}
        if keyword == "" or len(userlist) == 0:
            messages.success(request, "关键词不能为空或未查到相关用户信息")
        return render(request, "useradd.html", info)

    # 添加用户页面弹窗
    def userAddadd(request):
        return render(request, "useraddadd.html")
    #添加用户处理逻辑
    def userAddaction(requst):
        username=requst.POST.get("usernametext")
        password=requst.POST.get("password")
        roletext=requst.POST.get("roletext")
        if roletext == '0':
            rolename="歌手"
        else:
            rolename="购票人"
        print(username)
        print(password)
        print(rolename)
        if(len(password)<6 or len(password)>20):
            messages.success(requst, "添加失败，请检查用户信息是否符合规范")
            return render(requst,"useraddadd.html")
        if(cd.addUser(username,password,rolename)):
            messages.success(requst,"添加成功")
        else:
            messages.success(requst,"添加失败，请检查用户信息是否符合规范")
        return render(requst,"useraddadd.html")

    # 删除宿舍处理逻辑
    def userDeldel(request):
        user_name = request.POST.get("username")
        deluser_pk = request.POST.get("id")
        role = cd.find(user_name).role.rolename
        print(deluser_pk)
        if (cd.delUser(int(deluser_pk))):

            return HttpResponse(1)
        else:

            return HttpResponse(0)

    # 批量删除宿舍处理逻辑
    def userDeldelall(request):
        user_name = request.POST.get("username")
        deluser_pks = request.POST.get("ids")
         # print(delbuilding_pks)
        role = cd.find(user_name).role.rolename
        pks = analysis_str_list(deluser_pks)
        print(pks)
        flag = 1
        for id in pks:
            print(int(id))
            if (cd.delUser(int(id))):
                flag = 1
            else:
                flag = 0
        return HttpResponse(flag)