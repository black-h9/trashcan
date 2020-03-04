from django.urls import path,include

from . import views
urlpatterns = [

    #全局
    path('getBase',views.getBase,name = 'getBase'),

#  首页
    path('getIndex',views.getIndex,name = 'getIndex'),

#丢垃圾
    path('getAsh',views.getAsh,name = 'getAsh'),

#  注册
    path('getRegister',views.getRegister,name = 'getRegister'),

#  登陆
    path('getLogin',views.getLogin,name = 'getLogin'),

#  设置
    path('getSet',views.getSet,name = 'getSet'),

#验证码
    path('captcha', include('captcha.urls')),

#退出登陆
    path('exitLogin',views.exitLogin,name = 'exitLogin'),
#
#
#
#
#
#
#

]
