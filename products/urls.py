from django.urls import path, include
from . import views 
from .views import *

app_name = 'products'

urlpatterns = [ 
    # Página inicial
    path('', FeedView.as_view(), name="home"),
    # path("select2/", include("django_select2.urls")),

    # Páginas dos produtos
    path('products/add', NewProductView.as_view(), name='add'),
    path('products/<int:pk>/exchange/', exchange, name='exchange'),
    path('products/<int:user_pk>/<int:pk>/info', ProductView.as_view(), name='detail'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='update'),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='delete'),
]