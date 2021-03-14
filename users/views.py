# Misc
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import RedirectView
# Generic Views
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
# Auth 
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# My Forms & Models
from .forms import LoginForm, CreateUserForm, userAccount
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

@login_required
def detail_user(request):
    if(request.method == "POST"):
        form = userAccount(request.POST, request.FILES)
        if(form.is_valid()):
            data = form.cleaned_data
            user = request.user
            profile = user.profile
            passwd = data.get("password")
            confirm_passwd = data.get("confirm_password")
            
            if(data.get("bio")): profile.bio = data["bio"]
            if(data.get("date_of_birth")): profile.date_of_birth = data["date_of_birth"]
            if(data.get("profile_image")): profile.profile_image = data["profile_image"]
            
            if(passwd and confirm_passwd and passwd == confirm_passwd):
                user.set_password(passwd)
            
            profile.save()
            user.save()

    form = userAccount()

    return render(
        template_name= "users/detail.html",
        request=request,
        context={
            "form":form,
            "user":request.user,
        }
    )

class RedirectLogin(RedirectView):
    """ Redirects to my account page, after login"""
    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('users:my_account',kwargs={'pk': request.user.profile.pk }))
    