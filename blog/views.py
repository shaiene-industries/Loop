from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Class views

# See docs for ListView
# Lists all posts
class PostsView(ListView):
    model = Post
    template_name = "posts/home.html"

# See docs for DetailView
# Show the article in full detail
class ArticleView(DetailView):
    model = Post
    template_name = "posts/articleDetail.html"

# See docs for LoginRequiredMixin, UpdateView and reverse_lazy
# Allows user to change the content of the article
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/postForm.html'
    # form_class = PostForm
    login_url = reverse_lazy('blog:login')
    fields = ['title','body']
    success_url = reverse_lazy('blog:posts')

# See docs for LoginRequiredMixin and CreateView
# Allows user to create a new Article
class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/postForm.html'
    form_class = PostForm
    login_url = reverse_lazy('blog:login')

    # Overriding form_valid to associate the user to the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = reverse_lazy('blog:login')
    success_url = reverse_lazy('blog:posts')

#Function Views
# def base(request):
#     return render(request,'base/base.html',{})

# def home(request):
#     return render(request,'home.html', {})
