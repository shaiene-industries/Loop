from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
#from django.auth.
# Create your views here.

class CreateUser(CreateView):
    template_name = 'users/create.html'
    model = User
    fields = ['username', 'email', 'password']


