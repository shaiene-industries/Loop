from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import LoginForm, CreateUserForm
#from django.auth.
# Create your views here.


class CreateUser(CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = CreateUserForm

