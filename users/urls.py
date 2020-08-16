from django.urls import path 
from . import views # Use this for functions

app_name = 'users'

urlpatterns = [
    path('login',views.users, name='users'),
]
