from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Class views

# See docs for ListView
class PostsView(ListView):
    model = Post
    template_name = "posts/home.html"

# See docs for DetailView
class ArticleView(DetailView):
    model = Post
    template_name = "posts/articleDetail.html"

# See docs for LoginRequiredMixin, UpdateView and reverse_lazy
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/postForm.html'
    # form_class = PostForm
    login_url = reverse_lazy('blog:login')
    fields = ['title','body']
    success_url = "/posts"

# See docs for LoginRequiredMixin and CreateView
class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/postForm.html'
    form_class = PostForm
    login_url = reverse_lazy('blog:login')

    # Overriding form_valid to associate the user to the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#Function Views
# def base(request):
#     return render(request,'base/base.html',{})

# def home(request):
#     return render(request,'home.html', {})
