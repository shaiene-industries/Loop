from django.urls import path 
from . import views # Use this for functions
from .views import CreateUser # Use this for classes

app_name = 'users'

urlpatterns = [
    path('create',CreateUser.as_view(), name='create'),
    path('login',views.loginUser, name='login'),
]
