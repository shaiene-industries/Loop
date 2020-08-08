from django.urls import path
from . import views # Use this for functions

app_name = 'index'

urlpatterns = [
    path('',views.index, name="index"),
]