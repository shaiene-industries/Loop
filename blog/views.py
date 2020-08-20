from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# Class views
class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"

class ArticleView(DetailView):
    model = Post
    template_name = "posts/articleDetail.html"


class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/postForm.html'
    fields = ('title', 'author', 'body',)
    login_url = 'accounts/login/'



#Function Views
def base(request):
    return render(request,'base/base.html',{})

# def home(request):
#     return render(request,'home.html', {})
