from django.urls import path 
from . import views # Use this for functions
from .views import PostsView, ArticleView, NewPostView, UpdatePostView, DeletePostView # Use this for classes
from django.contrib.auth.views import LoginView

app_name = 'blog'

urlpatterns = [ 
    path('', PostsView.as_view(), name = "posts"),
    path('article/<int:pk>', ArticleView.as_view(), name='articleDetail'),
    path('article/<int:pk>/update', UpdatePostView.as_view(), name='articleUpdate'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='articleDelete'),
    path('postForm', NewPostView.as_view(), name='postForm'),
    path('accounts/login/', LoginView.as_view(template_name='auth/login.html'), name='login')
]