from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Class views
class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"

class ArticleView(DetailView):
    model = Post
    template_name = "posts/article-detail.html"

class NewPostView(CreateView):
    model = Post
    template_name = 'posts/postForm.html'
    fields = dict.fromkeys(["title","author","body"])
    def addPost():
        pass

def base(request):
    return render(request,'base/base.html',{})

# Create your views here.

# Function Views
# def home(request):
#     return render(request,'home.html', {})
