from django.urls import path 
from . import views 
from .views import *

app_name = 'products'

urlpatterns = [ 
    path('', PostsView.as_view(), name = "posts"),
    path('article/<int:pk>', ArticleView.as_view(), name='productDetail'),
    path('postForm', NewPostView.as_view(), name='postForm'),
]