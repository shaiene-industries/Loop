from django.urls import path 
from . import views 
from .views import CreateUser 
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    path('create',CreateUser.as_view(), name='create'),
    path('accounts/login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
]
