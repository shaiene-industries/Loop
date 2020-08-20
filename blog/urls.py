from django.urls import path 
from . import views # Use this for functions
from .views import HomeView, ArticleView, NewPostView # Use this for classes
from django.contrib.auth.views import LoginView

app_name = 'blog'

urlpatterns = [
    #path('', views.home, name="home" ) 
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ArticleView.as_view(), name='articleDetail'),
    path('postForm', NewPostView.as_view(), name='postForm'),
    path('base',views.base, name="base"),
    path('accounts/login/', LoginView.as_view(template_name='auth/login.html'), name='login')
]