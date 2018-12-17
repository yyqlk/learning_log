# AUTHOR : YYQLK
from django import forms
from django.contrib.auth.models import User
import re


class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

#
# class RegistrationFrom(forms.Form):
#
#     username = forms.CharField(label='Username', max_length=50)
#     email = forms.EmailField(label='Email',max_length=50)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
#     # username = forms.CharField(label='Username', max_length=50)
#     # password = forms.CharField(label='Password', widget=forms.PasswordInput)
