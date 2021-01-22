"""webrec_and_send URL Configuration

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
from websend import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first),
    #登录界面
    path('login/',views.first),
    #判断登录
    path('userLogin/',views.loginController),
    #获取信息
    path(r'^getdata/(?P<token>\w+)/$',views.getdata,name="getdata"),
    #用户信息主界面
    path('faninfo/',views.faninfo),
    #充值界面
    path(r'^addMoneyIndex/(?P<token>\w+)/$',views.addMoneyIndex,name="addMoneyIndex"),
    path('addMoneyIndexOther/',views.addMoneyIndexOther),
    #充值操作
    path(r'^addMoney/(?P<token>\w+)/$',views.addMoney,name="addMoney"),
    #开始购票界面
    path('start/',views.start),
    #查询已购票界面
    path(r'^search/(?P<username>\w+)/$',views.search,name="search"),
    #进入购票填写购买人数页面
    path('selectDorindex/',views.selectDorindex),
    #购票人数处理
    path('selectFirst/',views.selectDorFirst),
    path('selectSecond/',views.selectDorSecond,name="selectSecond"),
    #购票处理
    path(r'^selectDorAction/(?P<count>\w+)/(?P<concertname>\w+)/$',views.selectDorAction,name="selectDorAction")
]
