from django.urls import path, include
from . import views 
from .views import *

app_name = 'products'

urlpatterns = [ 
    # Página inicial
    path('', home, name="home"),

    # Páginas dos produtos
    path('products/feed', FeedView.as_view(), name = "feed"),
    path('products/add', NewProductView.as_view(), name='addProduct'),
    path('products/<int:pk>/info', ProductView.as_view(), name='productDetail'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='productUpdate'),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='productDelete'),
    
    
    # Template Base com a navbar
    path('base/', base, name="base"), 
    
]