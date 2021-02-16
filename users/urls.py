from django.urls import path 
from . import views 
from .views import CreateUser, LoginUser

app_name = 'users'

urlpatterns = [
    path('create',CreateUser.as_view(), name='signup'),
    path('accounts/login/', LoginUser.as_view(), name='login'),
]
