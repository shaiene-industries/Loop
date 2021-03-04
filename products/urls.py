from django.urls import path 
from . import views 
from .views import *

app_name = 'products'

urlpatterns = [ 
    # Página inicial
    path('', FeedView.as_view(), name="home"),

    # Páginas dos produtos
    path('products/add', NewProductView.as_view(), name='addProduct'),
    path('products/<int:user_pk>/<int:pk>/info', ProductView.as_view(), name='productDetail'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='productUpdate'),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='productDelete'),
]