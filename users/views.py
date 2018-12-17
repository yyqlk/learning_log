from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def login_view(request):
    """login"""
    if request.method != 'POST': # 第一次打开提供一个新表单
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("learning_logs:index"))
            else:
                print('登陆失败')
    return render(request, 'users/login.html', {'form': form,})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))





def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页

            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))
    return render(request, 'users/register.html', {'form': form })




