from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import LoginForm, CreateUserForm



class CreateUser(CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = CreateUserForm


class LoginUser(LoginView):
    template_name='users/login.html'
    authentication_form = LoginForm