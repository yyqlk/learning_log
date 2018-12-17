# AUTHOR : YYQLK
"""定义users的urls"""
from django.urls import path, re_path

from . import views

urlpatterns = [
    #  登录页面
    re_path('^login/$', views.login_view, name='login'),
    re_path('^logout',views.logout_view,name='logout'),
    re_path('^register', views.register, name='register'),
    re_path('^login_x', views.login_view, name='login_x')
]




