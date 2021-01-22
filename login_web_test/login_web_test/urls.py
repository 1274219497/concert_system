"""login_web_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sign import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    #登录
    path('userLogin/',views.UserController.userLogin),
    path('login/',views.login),
    #修改密码
    path('modifypasswordview/',views.UserController.modifyPasswordview),
    path(r'^modifypassword/(?P<username>\w+)/$',views.UserController.modifyPassword,name="mp"),
    #修改密码
    path('modifypasswordview_singer/',views.UserController.modifyPasswordview_singer),
    path(r'^modifypassword_singer/(?P<username>\w+)/$',views.UserController.modifyPassword_singer,name="mps"),
    #后台管理者主页
    path('index_teacher/',views.UserController.teacherWelcome),
    #歌手主页
    path('index_manager/',views.UserController.managerWelcome),
    #查询用户
    path('userlist/',views.UserController.userList),
    path(r'^usersearch1/(?P<username>\w+)/(?P<role>\w+)/$',views.UserController.userSearch1,name="usersearch1"),
    path('useredit/',views.UserController.userEdit),
    #编辑用户
    path(r'^usereditaction/(?P<username>\w+)/$',views.UserController.userEditaction,name="usereditaction"),
    #删除用户
    path('userdel/',views.UserController.userDel),
    path(r'^usersearch3/(?P<username>\w+)/(?P<role>\w+)/$',views.UserController.userSearch3,name="usersearch3"),
    path('userdeldel/', views.UserController.userDeldel),
    path('userdeldelall/', views.UserController.userDeldelall),
    #添加用户
    path('useradd/',views.UserController.userAdd),
    path(r'^usersearch2/(?P<username>\w+)/(?P<role>\w+)/$',views.UserController.userSearch2,name="usersearch2"),
    path('useraddadd/',views.UserController.userAddadd),
    path('useraddaction/',views.UserController.userAddaction),
    #统计
    path('show/',views.show),
    #统计（歌手）
    path('show_singer/',views.show_singer),
    #退出
    path('ret/',views.ret)
]
