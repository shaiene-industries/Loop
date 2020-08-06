from django.urls import path 
from . import views # Use this for functions
from .views import HomeView, ArticleView, NewPostView # Use this for classes

app_name = 'blog'

urlpatterns = [
    #path('', views.home, name="home" ) 
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ArticleView.as_view(), name='article-detail'),
    path('postForm', NewPostView.as_view(), name='postForm'),
    path('base',views.base, name="base"),
]