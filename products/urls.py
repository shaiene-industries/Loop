from django.urls import path 
from . import views 
from .views import *

app_name = 'products'

urlpatterns = [ 
    # Página inicial
    path('', FeedView.as_view(), name="home"),

    # Páginas dos produtos
    path('products/<int:pk>/exchange/', exchange, name='exchange'),
]