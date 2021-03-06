# Misc
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import RedirectView
# Generic Views
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Auth 
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# My Forms & Models
from .forms import LoginForm, CreateUserForm
from .models import Profile


class CreateUser(CreateView):
    """ Criação (registro) de usuário """
    template_name = 'users/create.html'
    form_class = CreateUserForm
    # def get_success_url(self):
    #     return reverse('products:home')
    def get_success_url(self):
        return reverse('users:minha_conta',kwargs={'pk': self.object.profile.pk})

class LoginUser(LoginView):
    """" Tela de Login de Usuário """
    template_name ='users/login.html'
    authentication_form = LoginForm

class DetailUser(DetailView, LoginRequiredMixin):
    """" Página da minha conta do Usuário. Trabalha com o objeto Profile."""
    template_name = 'users/detail.html'
    model = Profile

class RedirectLogin(RedirectView):
    """ Redireciona para a página da minha conta após o login."""
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('users:minha_conta',kwargs={'pk': request.user.profile.pk }))
    